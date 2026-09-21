"""Deux controles sur le site, a relancer plutot qu'a croire.

1. **Couverture des classes** : toute classe utilisee dans le HTML a-t-elle une regle dans la
   feuille de style ? Attrape une classe inventee en ecrivant une page, et un bloc CSS supprime a
   tort en nettoyant.

2. **Contraste WCAG 2.2 AA** : les couleurs de la palette passent-elles les seuils ? ⚠️ On MESURE,
   on ne relit pas. La lecon du parc est qu'une palette annoncee a deux couleurs en a huit en
   vrai, et qu'un contraste juge « suffisant » a l'oeil ne l'est pas.

Usage :
  python scripts/verifier-site.py

⚠️ Ce script a d'abord ete ecrit comme jetable puis supprime, et il a fallu le reecrire le jour
meme. Un controle qu'on veut pouvoir relancer n'est pas du jetable : il se versionne.
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAGES = sorted(p.name for p in RACINE.glob("*.html"))
CSS = (RACINE / "style.css").read_text(encoding="utf-8")

# Classes posees par le script a l'execution, absentes du HTML au repos.
DYNAMIQUES = {"visible"}


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


def main() -> int:
    echecs = 0
    print(f"Pages examinees : {', '.join(PAGES)}")

    print("-- Couverture des classes --")
    manquantes = {
        classe: pages
        for classe, pages in classes_du_html().items()
        if classe not in DYNAMIQUES and not re.search(rf"\.{re.escape(classe)}[\s,:.{{\[]", CSS)
    }
    if manquantes:
        echecs += 1
        for classe, pages in sorted(manquantes.items()):
            print(f"  ECHEC : .{classe} sans regle, utilisee dans {', '.join(sorted(pages))}")
    else:
        print("  OK : chaque classe du HTML a une regle.")

    print("-- Contraste WCAG 2.2 AA --")
    fond, carte = variable("--bg"), variable("--card")
    # 4,5:1 pour le texte courant, 3:1 pour le texte large et les elements non textuels.
    paires = [
        ("texte courant sur le fond", variable("--text"), fond, 4.5),
        ("texte courant sur une carte", variable("--text"), carte, 4.5),
        ("texte atenue sur le fond", variable("--muted"), fond, 4.5),
        ("texte atenue sur une carte", variable("--muted"), carte, 4.5),
        ("texte atenue sur le fond secondaire", variable("--muted"), variable("--bg2"), 4.5),
        ("lien sur le fond", variable("--blue-l"), fond, 4.5),
        ("lien sur une carte", variable("--blue-l"), carte, 4.5),
        ("texte blanc sur bouton plein", "#ffffff", variable("--blue-d"), 4.5),
        ("accent sur le fond (gros titre)", variable("--blue"), fond, 3.0),
        ("ambre de l'avertissement sur le fond", variable("--orange"), fond, 3.0),
    ]
    for libelle, avant, apres, seuil in paires:
        ratio = contraste(avant, apres)
        if ratio < seuil:
            echecs += 1
        verdict = "OK " if ratio >= seuil else "ECHEC"
        print(f"  {verdict} {libelle:38s} {avant} sur {apres} = {ratio:.2f}:1 (seuil {seuil})")

    print("-- Resultat --")
    print("  tout passe." if not echecs else f"  {echecs} probleme(s).")
    return 1 if echecs else 0


if __name__ == "__main__":
    # ⚠️ Windows rend un `UnicodeEncodeError` sur une sortie non ASCII en cp1252 : piege documente
    # du parc, on force l'encodage plutot que de renoncer aux accents.
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
