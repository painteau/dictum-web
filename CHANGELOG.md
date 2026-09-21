# Changelog

Toutes les évolutions notables de `dictum-web` sont documentées ici.

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versionnage
[SemVer](https://semver.org/lang/fr/). La section `[Unreleased]` accumule au fil de l'eau et
est renommée en numéro de version au moment de poser le tag.

Ce fichier est créé le 2026-09-05, après la mise en service : les évolutions antérieures ne sont
pas reconstituées, ce qui serait de la réécriture d'historique plutôt que de la documentation.

⛔ **L'historique git a été écrasé en un commit le 2026-09-21**, donc il n'est plus la source de
vérité pour ce qui précède cette date, contrairement à ce que cette section affirmait. Ce fichier
est désormais le seul récit de ce dépôt.

## [Unreleased]

## [1.1.0] - 2026-09-21

### Modifié

- **La page d'accueil était écrite par un ingénieur pour des ingénieurs, elle est réécrite pour la
  personne qui va s'en servir.** Elle annonçait des tailles de modèles en mégaoctets, des noms de
  moteurs graphiques, des recettes de terminal et des mesures de vitesse. Tout cela est vrai et
  n'a aucune place sur la première page d'un produit destiné à des gens qui ne connaissent rien à
  l'informatique.

  ⚠️ **Le public visé n'est pas « le grand public », c'est plus précis que ça** : des professions
  tenues au secret, qui ont une raison concrète et parfois réglementaire de ne pas laisser sortir
  ce qu'elles dictent. Médecins, avocats, notaires, journalistes, experts-comptables. Pour elles,
  un logiciel de dictée local n'est pas un confort, et la page le dit dans ces termes.

  La page nomme donc **le problème avant la solution** (les autres outils de dictée envoient la
  voix à un serveur), puis à qui ça parle, puis ce que ça change concrètement : sans prestataire,
  il n'y a ni contrat à signer, ni sous-traitant à inscrire sur un registre, ni pays d'hébergement
  à vérifier.

  ⚠️ **Elle s'arrête volontairement avant la promesse juridique** : un encart dit noir sur blanc
  que nous décrivons le fonctionnement du logiciel et pas la situation réglementaire du lecteur.
  Annoncer une conformité que nous ne sommes pas en position de garantir serait exactement le
  genre d'affirmation que ce public est entraîné à vérifier.

- **La preuve proposée au lecteur ne demande aucune compétence** : couper le wifi et dicter. Un
  logiciel qui envoie la voix ailleurs ne peut pas fonctionner sans réseau. C'est un meilleur
  argument que n'importe quelle description d'architecture, et c'est vérifiable par la personne
  elle-même en dix secondes.

- **Les limites sont sur la page d'accueil et rendues actionnables**, pas reléguées en notes de
  version : pas de version Mac, et sous Linux pas encore de Wayland, avec la précision que c'est
  le choix par défaut des versions récentes d'Ubuntu et de Fedora. Sans cette précision, le mot
  « Wayland » ne dit rien à personne et l'avertissement ne sert à rien.

### Ajouté

- **L'application iPhone est annoncée**, ce que la refonte précédente avait complètement oublié
  alors qu'elle sort bientôt. Même principe : la reconnaissance vocale s'exécute sur l'appareil.

  ⛔ **Et la seule fonction qui enverrait du texte ailleurs est annoncée comme telle, en encart.**
  L'aide à la rédaction a besoin d'un modèle qu'un téléphone ne peut pas faire tourner ; elle est
  **désactivée par défaut** et l'activer demande le compte personnel de l'utilisateur chez le
  fournisseur de son choix. Le relevé du code de l'application a été fait avant d'écrire cette
  ligne, précisément parce qu'une promesse trop large ici casserait devant le seul public qui la
  lira attentivement. Aucune date annoncée.

- **Une page « détails techniques »** qui recueille tout ce qui a quitté l'accueil : whisper.cpp,
  les trois modèles et les trois moteurs avec leurs mesures, les recettes apt et pacman, les
  limites, la licence, et **les emplacements exacts où les dictées sont écrites sur le disque**
  pour les trois systèmes. Ce dernier point n'est pas de la curiosité technique : quelqu'un qui
  dicte des comptes rendus de consultation a le droit de savoir où ils sont.

- **Une foire aux questions qui répond aux objections réelles** plutôt qu'aux fonctionnalités :
  où est le piège si c'est gratuit, comment en être sûr, est-ce que ça remplace une secrétaire
  (non, et c'est dit), combien de temps ça prend, et que se passe-t-il si on change d'avis. Elle
  utilise `details`/`summary` natifs, donc elle s'ouvre au clavier et se lit par un lecteur
  d'écran sans une ligne de JavaScript, et elle est déclarée en `FAQPage` pour les moteurs.

- **`scripts/verifier-site.py`, versionné et prouvé rouge** : vérifie que toute classe du HTML a
  une règle CSS, et **mesure** les contrastes WCAG 2.2 AA au lieu de les relire.

  ⚠️ **Ce script avait d'abord été écrit comme jetable, supprimé au nettoyage, puis redemandé
  dans la même heure.** Un contrôle qu'on veut pouvoir relancer n'est pas du jetable : il se
  versionne. Sa suppression avait de surcroît fait passer la couverture des classes de quatre
  pages à deux sans que rien ne le signale.


## [1.0.0] - 2026-09-21

Réécriture complète. **Majeure assumée** : le site décrivait un logiciel qui n'existe plus, et il
servait des fichiers que ce logiciel téléchargeait à l'exécution. Les deux disparaissent.

### Corrigé

- **Le site annonçait un produit qui n'existe plus, et presque chaque affirmation était fausse.**
  Il présentait Dictum 1.7.0, alors que le logiciel a été repris de zéro et sort en 0.1.1. Ce qui
  était annoncé et n'existe pas : transcription en continu, reformulation par un modèle local,
  API HTTP sur le port 44880, glisser-déposer de fichiers audio, plus de trente commandes en ligne
  de commande, et une extension VS Code dont **le dépôt était introuvable**.

  ⚠️ **Le chiffre le plus révélateur était « 57 langues »** : l'interface n'en propose que trois,
  français, anglais et détection automatique. Whisper en sait davantage, l'application ne les
  expose pas. Un chiffre juste sur la bibliothèque et faux sur le produit.

- **Le site annonçait une licence MIT sur trois dépôts, dont aucun ne la portait comme annoncé.**
  Le fichier existait bien sur l'ancien dépôt, mais au nom de `painteau` et non de l'association,
  ce que la règle du parc interdit. L'ancien dépôt est désormais privé et archivé, et le nouveau
  porte **BZ-1.1**, qui est une licence en accès libre et **pas** une licence open source au sens
  de l'OSI. Le site le dit maintenant dans ces termes.

- **Le bouton de téléchargement pointait vers les releases d'un dépôt qui vient de passer en
  privé.** Il vise désormais le **nom fixe** sur `dl.breizhzion.com`, que la chaîne de publication
  écrase à chaque sortie, et la version affichée est **lue** dans `latest.json` au lieu d'être
  écrite en dur. C'est la leçon du site de Hublot, qui a distribué une version vieille de six
  sorties en répondant `200` à chaque fois : un lien périmé ne casse rien de visible, donc rien ne
  le signale.

### Ajouté

- **Des procédures d'installation pour les trois systèmes**, en onglets : installateur Windows,
  dépôt apt pour Debian et Ubuntu, dépôt pacman pour Arch. ✅ **Les deux recettes Linux ont été
  jouées telles qu'elles sont affichées**, dans des conteneurs neufs, jusqu'à `dictum --version`.
  La recette pacman a été vérifiée avec `pacman-key --lsign-key apt@breizhzion.com`, la forme par
  adresse que la page publie, et pas seulement avec l'empreinte.

- **Ce que le logiciel ne fait pas encore, écrit sur la page d'accueil et pas seulement dans les
  notes de version** : sous Linux la dictée fonctionne sur X11 et pas sur Wayland, et sur macOS
  elle n'est pas disponible. Quelqu'un doit pouvoir le découvrir avant d'installer.

- **Les mesures de vitesse plutôt que des adjectifs** : les durées des trois modèles et le gain
  d'une carte graphique sont ceux qui ont été relevés, et la page dit sur quoi.

- **Une page 404, qui manquait.** Sans elle, Cloudflare Pages renvoie la page d'accueil en `200`
  pour n'importe quel chemin absent. ⚠️ **C'est ce qui a fait échouer ma propre vérification** que
  les binaires whisper avaient bien disparu : ils répondaient `200`, et j'ai conclu qu'ils étaient
  toujours servis, alors que le corps était du HTML et le `Content-Type` `text/html`. Mesurer un
  code de statut là où il faut mesurer le contenu, c'est exactement le piège que le parc a déjà
  payé sur un lien de téléchargement périmé.

### Supprimé

- **Les six binaires whisper.cpp et `manifest.json`.** Ce n'étaient pas des ornements : l'ancien
  logiciel lisait ce manifeste **à l'exécution** pour savoir où télécharger ses moteurs, donc le
  site était une API et pas une vitrine. Ils partent parce que ce logiciel est abandonné et que
  personne ne l'a installé. `NOTICE.md` part avec eux, les notices tierces vivant désormais dans
  le dépôt du logiciel, qui est celui qui redistribue.

  ⚠️ **`announcements.json` reste**, lui : c'est l'application mobile qui le lit, et elle a de
  vrais utilisateurs sur TestFlight.

- **L'historique git du dépôt, écrasé en un commit.** ⚠️ **Conséquence directe : l'avertissement en
  tête de ce fichier, qui désignait l'historique git comme source de vérité pour ce qui précède le
  2026-09-05, est devenu faux.** Il a été corrigé dans le même geste.


## [0.2.0] - 2026-09-12

### Corrigé

- **Le site n'affichait pas le logo de l'application, et pas moins de trois marques différentes y
  coexistaient.** Le favicon de l'onglet portait un disque bleu plein évidé en son centre ; les
  en-têtes portaient une variante à anneau translucide (`opacity: .6`) ; les pieds de page
  reprenaient encore le favicon. Or la marque Dictum est un **disque central entouré d'un anneau
  séparé**. Les quatre emplacements (en-tête et pied de page des deux pages) plus `favicon.svg`
  portent désormais la géométrie **relevée sur l'icône de l'application** (`bzhzion/dictum-app`,
  `assets/icon.png`, générée par `scripts/generer_icones.py`) : disque `r=6`, anneau de `r=11` à
  `r=13`.
- L'anneau est tracé en **`stroke` centré sur `r=12`, épaisseur 2**, ce qui est exactement
  équivalent aux deux cercles pleins mais ne peint **rien** entre le disque et l'anneau. Le motif
  reste donc juste sur n'importe quel fond, là où la variante précédente peignait un `#121218` en
  dur qui ne tombait juste que sur la couleur de page d'alors.
- Vérifié plutôt que supposé : le `logo` des données structurées pointe bien vers
  `breizhzion.com/favicon.svg`, mais il appartient au nœud **Organization** de Breizhzion et non à
  Dictum. Il est donc **correct** et n'a pas été touché.

### Ajouté

- **`announcements.json`** : fichier d'annonces lu par l'app mobile Dictum au démarrage, qui
  permet de pousser un message aux utilisateurs **sans passer par une mise à jour publiée sur
  l'App Store**. Publié vide (`"announcements": []`), avec le format et les bornes documentés
  dans le fichier lui-même. Motif du kit mobile partagé (`admin/.claude/mobile-kit/`), même
  mécanisme que `appermittent` et `maeil`. Règle à ne pas enfreindre : ne jamais réutiliser un
  `id` déjà publié, un appareil qui l'a déjà vu ne le reverra jamais.

### Corrigé

- **Convention de fins de ligne du parc posée dans `.gitattributes`.** Le bloc `run:` d'un
  workflow GitHub Actions est un script shell exécuté sur un runner Linux : un antislash de
  continuation suivi d'un retour chariot **ne continue pas** la ligne, la commande est coupée en
  deux, et le message d'erreur ne parle jamais de fins de ligne.
- Cas réel du 2026-09-07 sur `bzhzion/cabanon` : un `.yml` recommité en CRLF depuis une machine
  Windows (où `core.autocrlf` est actif) a fait échouer le déploiement de l'API sur un
  `usage: ssh`, la destination de la commande ayant disparu avec la continuation.
- LF forcé sur ce qu'exécute Linux (`*.sh`, `*.yml`, `*.yaml`, `Dockerfile`), CRLF sur ce
  qu'exécute Windows (`*.ps1`, `*.bat`, `*.cmd`), et `* text=auto` comme filet général.
  Référence : `admin/.claude/gitattributes-parc`.


## [0.1.0] - 2026-09-05

### Ajouté

- **Convention changelog du parc posée sur ce dépôt** : ce fichier, les hooks `pre-commit` et
  `pre-push` dans `.githooks/`, et le workflow `changelog-guard.yml` qui rejoue les mêmes
  contrôles en CI au moment du tag. Ce dépôt en était dépourvu alors qu'il est déployé, ce qui
  le laissait hors de la garantie que les autres ont.

