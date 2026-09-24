"""Signale les pages du site aux moteurs qui acceptent IndexNow.

Pourquoi ce protocole et pas un autre : il ne demande **aucun compte**. La preuve de propriete est
un fichier contenant la cle, servi a la racine du site ; le moteur va le lire avant d'accepter le
signalement. Bing, Yandex, Seznam et Naver le partagent entre eux.

⛔ **Google n'utilise pas IndexNow**, et son ancien signalement de sitemap a ete retire en 2023 :
pour lui, il n'existe plus de chemin automatique. Le sitemap declare dans `robots.txt` reste le
seul levier, avec les liens entrants. Ce script ne pretend donc pas couvrir Google, et c'est
volontairement ecrit ici pour que personne ne le croie.

⚠️ **Les URL signalees sont DERIVEES du sitemap**, jamais recopiees a la main : une liste tenue en
double finit par diverger de celle qui fait autorite, et on signalerait alors une page qui n'existe
plus ou on en oublierait une neuve.

Usage :
  python scripts/signaler-indexnow.py            signale
  python scripts/signaler-indexnow.py --verifier  controle la cle et les URL sans rien envoyer
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
HOTE = "oyant.breizhzion.com"
POINT_DE_COLLECTE = "https://api.indexnow.org/indexnow"


def cle() -> str:
    """La cle est le NOM du fichier a la racine, et son contenu : les deux doivent concorder."""
    fichiers = [f for f in RACINE.glob("*.txt") if re.fullmatch(r"[0-9a-f]{8,128}", f.stem)]
    if len(fichiers) != 1:
        raise SystemExit(
            f"{len(fichiers)} fichier de cle a la racine, il en faut exactement un "
            "(un nom de 8 a 128 caracteres hexadecimaux, suivi de .txt)"
        )
    fichier = fichiers[0]
    contenu = fichier.read_text(encoding="utf-8").strip()
    if contenu != fichier.stem:
        raise SystemExit(
            f"le fichier {fichier.name} contient « {contenu} » au lieu de « {fichier.stem} » : "
            "le moteur refusera le signalement"
        )
    return contenu


def urls() -> list[str]:
    sitemap = (RACINE / "sitemap.xml").read_text(encoding="utf-8")
    trouvees = re.findall(r"<loc>([^<]+)</loc>", sitemap)
    if not trouvees:
        raise SystemExit("aucune URL dans sitemap.xml")
    return trouvees


def main() -> int:
    valeur = cle()
    liste = urls()

    print(f"cle : {valeur}")
    print(f"servie a : https://{HOTE}/{valeur}.txt")
    print(f"{len(liste)} URL derivees du sitemap :")
    for url in liste:
        print(f"  {url}")

    if "--verifier" in sys.argv:
        print("\nverification seule, rien n'a ete envoye.")
        return 0

    corps = json.dumps(
        {
            "host": HOTE,
            "key": valeur,
            "keyLocation": f"https://{HOTE}/{valeur}.txt",
            "urlList": liste,
        }
    ).encode()

    requete = urllib.request.Request(POINT_DE_COLLECTE, data=corps, method="POST")
    requete.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(requete) as reponse:
            code = reponse.status
    except urllib.error.HTTPError as erreur:
        # ⚠️ 422 veut dire que la cle n'a pas pu etre lue a l'URL annoncee, donc presque toujours
        # que le site n'a pas encore ete deploye avec le fichier de cle.
        print(f"\nrefus HTTP {erreur.code} : {erreur.read().decode()[:200]}", file=sys.stderr)
        if erreur.code == 422:
            print("  la cle n'est probablement pas encore servie en ligne.", file=sys.stderr)
        return 1

    # 200 et 202 sont tous deux des acceptations : 202 signifie « recu, cle en cours de
    # verification ». Ni l'un ni l'autre ne promet une indexation, seulement une prise en compte.
    print(f"\nreponse : HTTP {code}" + (" (accepte)" if code in (200, 202) else ""))
    return 0 if code in (200, 202) else 1


if __name__ == "__main__":
    # ⚠️ stderr AUSSI, et pas seulement stdout : les refus du garde-fou de cle partent par la, et
    # c'est precisement le message qui doit rester lisible. Sans cette ligne, les guillemets et
    # les accents sortent en mojibake sur une console Windows.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
