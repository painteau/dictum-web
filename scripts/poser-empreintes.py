"""Pose une empreinte de CONTENU dans l'URL des ressources, pour que le cache ne serve jamais une
version perimee.

⛔ Le defaut mesure le 2026-09-21 : `style.css` etait servi avec `max-age=14400`, sans empreinte
dans son nom. Un visiteur passe dans les quatre heures precedentes continuait donc de recevoir
l'ANCIENNE feuille, et c'est exactement ce qui est arrive pendant les essais : le navigateur
calculait encore `Segoe UI` pour le titre alors que la feuille servie declarait bien Fraunces. Rien
ne le signalait, la page etant simplement d'une autre epoque.

Deux remedes possibles. Raccourcir le cache fait payer une revalidation a chaque visite et laisse
la fenetre de peremption ouverte. Mettre l'empreinte dans l'URL la ferme pour de bon : l'URL change
des que le contenu change, donc un cache long devient non seulement acceptable mais souhaitable.

⚠️ **L'empreinte est DERIVEE du contenu, jamais un numero de version ecrit a la main.** Un numero a
cote du fichier qu'il decrit finit toujours par mentir, et surtout un cache-buster qui contient une
version en clair la divulgue.

Usage :
  python scripts/poser-empreintes.py               pose les empreintes
  python scripts/poser-empreintes.py --verifier    sort en 1 si une empreinte est perimee
"""

import hashlib
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Ressource -> longueur de l'empreinte. Seules les ressources SANS empreinte dans leur nom de
# fichier en ont besoin. Les polices n'y sont pas : leur nom porte deja la famille et la coupe, et
# remplacer un dessin sans changer de nom ne se fait pas.
RESSOURCES = {"style.css": 8}


def empreinte(chemin: Path, longueur: int) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()[:longueur]


def pages() -> list[Path]:
    return sorted(RACINE.glob("*.html"))


def main() -> int:
    verifier = "--verifier" in sys.argv
    ecarts = 0
    touches = 0

    for ressource, longueur in RESSOURCES.items():
        fichier = RACINE / ressource
        if not fichier.is_file():
            print(f"erreur : {ressource} introuvable", file=sys.stderr)
            return 1
        attendue = empreinte(fichier, longueur)

        # ⚠️ Le motif accepte une URL avec OU sans empreinte : sans ca, la premiere pose
        # echouerait, et c'est precisement le cas qu'on ne teste jamais. Meme famille de piege
        # qu'une premiere publication qui n'est pas une mise a jour.
        motif = re.compile(rf'(["\'(]){re.escape(ressource)}(\?v=[0-9a-f]+)?(["\')])')

        for page in pages():
            texte = page.read_text(encoding="utf-8")
            trouvees = motif.findall(texte)
            if not trouvees:
                continue
            presentes = {t[1] for t in trouvees}
            voulue = {f"?v={attendue}"}
            if presentes == voulue:
                continue

            if verifier:
                ecarts += 1
                actuelles = ", ".join(sorted(p or "(aucune)" for p in presentes))
                print(f"  PERIMEE {page.name} : {ressource} porte {actuelles}, attendu ?v={attendue}")
                continue

            nouveau = motif.sub(rf"\g<1>{ressource}?v={attendue}\g<3>", texte)
            page.write_text(nouveau, encoding="utf-8", newline="")
            touches += 1
            print(f"  {page.name} : {ressource} -> ?v={attendue}")

    if verifier:
        if ecarts:
            print(f"\n{ecarts} empreinte(s) perimee(s). Lancer : python scripts/poser-empreintes.py")
            return 1
        print("OK : chaque empreinte correspond au contenu servi.")
        return 0

    print("Aucune empreinte a mettre a jour." if not touches else f"{touches} page(s) mise(s) a jour.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
