"""Deux controles sur le site, a relancer plutot qu'a croire.

1. **Couverture des classes** : toute classe utilisee dans le HTML a-t-elle une regle dans la
   feuille de style ? Attrape une classe inventee en ecrivant une page, et un bloc CSS supprime a
   tort en nettoyant.

2. **Contraste WCAG 2.2 AA** : les couleurs passent-elles les seuils ? ⚠️ On MESURE, on ne relit
   pas. La lecon du parc est qu'une palette annoncee a deux couleurs en a huit en vrai, et qu'un
   contraste juge « suffisant » a l'oeil ne l'est pas. Le controle se fait en deux temps : les
   paires qu'on a pense a nommer, puis un **balayage des couleurs ecrites en dur**, que par
   definition aucune liste tenue a la main ne retrouve.

Usage :
  python scripts/verifier-site.py

Deux lecons payees en ecrivant ce fichier, et gardees ici parce qu'elles se reperdent :

⚠️ Il a d'abord ete ecrit comme jetable puis supprime au nettoyage, et il a fallu le reecrire
dans l'heure. Un controle qu'on veut pouvoir relancer n'est pas du jetable, il se versionne.

⛔ Sa ligne de balayage a ete introduite par un heredoc de shell, ou le `\\b` de la regex est
devenu un **caractere de retour arriere invisible**. Le fichier s'affichait normalement et le
balayage annoncait « aucune couleur en dur » alors qu'il y en avait deux : un garde-fou qui mentait
exactement comme la regle du parc annonce que ce piege se manifeste. Ne jamais faire passer du
contenu de fichier par un heredoc.
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAGES = sorted(p.name for p in RACINE.glob("*.html"))
CSS = (RACINE / "style.css").read_text(encoding="utf-8")

# Classes posees par le script a l'execution, absentes du HTML au repos.
DYNAMIQUES = {"visible"}

# Fond des blocs de code : il ne vient pas d'une variable, donc il est nomme ici.
FOND_CODE = "#0a0a12"


def classes_du_html() -> dict[str, set[str]]:
    """Rend, pour chaque classe, l'ensemble des pages qui l'utilisent."""
    trouvees: dict[str, set[str]] = {}
    for page in PAGES:
        texte = (RACINE / page).read_text(encoding="utf-8")
        for attribut in re.findall(r'class="([^"]+)"', texte):
            for classe in attribut.split():
                trouvees.setdefault(classe, set()).add(page)
    return trouvees


def canal(valeur: float) -> float:
    valeur /= 255
    return valeur / 12.92 if valeur <= 0.03928 else ((valeur + 0.055) / 1.055) ** 2.4


def luminance(hexa: str) -> float:
    hexa = hexa.lstrip("#")
    r, v, b = (int(hexa[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * canal(r) + 0.7152 * canal(v) + 0.0722 * canal(b)


def contraste(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def variable(nom: str) -> str:
    trouve = re.search(rf"{re.escape(nom)}:\s*(#[0-9a-fA-F]{{6}})", CSS)
    if not trouve:
        raise SystemExit(f"variable {nom} introuvable dans style.css")
    return trouve.group(1)


def couverture_des_classes() -> int:
    print("-- Couverture des classes --")
    manquantes = {
        classe: pages
        for classe, pages in classes_du_html().items()
        if classe not in DYNAMIQUES and not re.search(rf"\.{re.escape(classe)}[\s,:.{{\[]", CSS)
    }
    if not manquantes:
        print("  OK : chaque classe du HTML a une regle.")
        return 0
    for classe, pages in sorted(manquantes.items()):
        print(f"  ECHEC : .{classe} sans regle, utilisee dans {', '.join(sorted(pages))}")
    return 1


def paires_nommees() -> int:
    print("-- Contraste WCAG 2.2 AA, paires nommees --")
    fond, carte = variable("--bg"), variable("--card")
    # 4,5:1 pour le texte courant, 3:1 pour le grand texte et les elements non textuels.
    paires = [
        ("texte courant sur le fond", variable("--text"), fond, 4.5),
        ("texte courant sur une carte", variable("--text"), carte, 4.5),
        ("texte atenue sur le fond", variable("--muted"), fond, 4.5),
        ("texte atenue sur une carte", variable("--muted"), carte, 4.5),
        ("texte atenue sur le fond secondaire", variable("--muted"), variable("--bg2"), 4.5),
        ("lien sur le fond", variable("--blue-l"), fond, 4.5),
        ("lien sur une carte", variable("--blue-l"), carte, 4.5),
        ("texte blanc sur bouton plein", "#ffffff", variable("--blue-d"), 4.5),
        ("numero de section sur le fond", variable("--blue"), fond, 4.5),
        ("accent sur le fond (grand texte)", variable("--blue"), fond, 3.0),
        ("ambre de l'avertissement sur le fond", variable("--orange"), fond, 3.0),
    ]
    echecs = 0
    for libelle, devant, derriere, seuil in paires:
        ratio = contraste(devant, derriere)
        if ratio < seuil:
            echecs += 1
        verdict = "OK " if ratio >= seuil else "ECHEC"
        print(f"  {verdict} {libelle:38s} {devant} sur {derriere} = {ratio:.2f}:1 (seuil {seuil})")
    return echecs


def balayage_des_couleurs_en_dur() -> int:
    """Eprouve chaque couleur de TEXTE ecrite en dur contre le pire fond du site.

    Le `(?<!-)` ecarte `background-color` et `border-color` : seules les couleurs de texte sont
    soumises au seuil de 4,5:1.
    """
    print("-- Contraste, balayage des couleurs de texte en dur --")
    fonds = {
        "--bg": variable("--bg"),
        "--bg2": variable("--bg2"),
        "--card": variable("--card"),
        "fond des blocs de code": FOND_CODE,
    }
    en_dur = sorted(set(re.findall(r"(?<!-)color:\s*(#[0-9a-fA-F]{6})", CSS)))
    if not en_dur:
        print("  aucune couleur de texte en dur, tout passe par une variable.")
        return 0

    echecs = 0
    for couleur in en_dur:
        ratio, nom = min((contraste(couleur, f), nom) for nom, f in fonds.items())
        # On ne peut pas savoir depuis la feuille si la couleur sert a du grand texte : on
        # applique donc le seuil le plus exigeant.
        if ratio < 4.5:
            echecs += 1
        verdict = "OK " if ratio >= 4.5 else "ECHEC"
        print(f"  {verdict} {couleur} au pire sur {nom:24s} = {ratio:.2f}:1 (seuil 4.5)")
    return echecs


def main() -> int:
    print(f"Pages examinees : {', '.join(PAGES)}")
    echecs = couverture_des_classes() + paires_nommees() + balayage_des_couleurs_en_dur()
    print("-- Resultat --")
    print("  tout passe." if not echecs else f"  {echecs} probleme(s).")
    return 1 if echecs else 0


if __name__ == "__main__":
    # ⚠️ Windows rend un `UnicodeEncodeError` sur une sortie non ASCII en cp1252 : piege documente
    # du parc, on force l'encodage plutot que de renoncer aux accents.
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
