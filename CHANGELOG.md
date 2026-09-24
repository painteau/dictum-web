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

### Changed

- ⛔ **Le produit s'appelle Oyant, et le site avec.** Une application **« Dictum - private voice
  to text »** existe déjà sur l'App Store (Factory Design LLC, `6759581003`) : même nom, même
  sous-titre sur l'absence de cloud, même traitement sur l'appareil, même gratuité. Ce n'était pas
  une homonymie mais un doublon, et tout le référencement construit ici envoyait les lecteurs
  chez quelqu'un d'autre.

  Le site répond désormais sur **`oyant.breizhzion.com`**, ajouté au même projet Pages.
  `dictum.breizhzion.com` continue de servir, le temps que les moteurs suivent.

  ⛔ **Les 13 liens « Code source » étaient MORTS entre le renommage du dépôt et ce commit.**
  GitHub n'a pas redirigé `bzhzion/dictum-desktop` vers `bzhzion/oyant-desktop` : l'ancienne
  adresse rend un vrai 404, y compris pour un navigateur. Ne pas compter sur cette redirection.

  ⚠️ **Les URL de téléchargement n'ont délibérément PAS été renommées.** Elles désignent des
  objets R2 qui existent, et que le site sert en ce moment. Les changer avant d'avoir copié les
  objets transformerait un téléchargement qui marche en 404, ce qui est exactement le défaut que
  ce dépôt a déjà payé sur un autre site. Règle appliquée : **on copie vers le nouveau préfixe,
  on ne déplace jamais.**

  ⚠️ **« Oyant » commence par une voyelle.** Le renommage mécanique a produit « de Oyant » et
  « que Oyant » dans cinq fichiers, y compris dans des `<title>` et du `schema.org`. Corrigé
  séparément : aucun contrôle automatique ne voit une élision fautive.

### Ajouté

- **Page de comparaison**, `/comparatif`. C'était le manque le plus coûteux du site : la question
  que se pose réellement quelqu'un qui cherche un logiciel de dictée est « lequel prendre », et
  nous n'avions aucune page qui y répondait. Les concurrents en ont, et c'est ce contenu-là que
  les moteurs de réponse citent.

  ⚠️ **Elle dit aussi ce que les autres font mieux**, et nomme les cas où il vaut mieux prendre un
  logiciel payant : version pour Mac, vocabulaire métier déjà chargé, insertion dans un logiciel
  patient, pédaliers, assistance joignable. Une page de comparaison qui ne perd jamais n'est pas
  lue comme une comparaison.

  ⛔ **Elle écrit noir sur blanc que Dictum n'est pas le seul à transcrire en local.** D'autres
  éditeurs font le même choix technique, et le laisser croire aurait été faux. Ce qui nous
  distingue est ailleurs, et l'argument tient mieux une fois dit honnêtement.

  ⚠️ **Les faits sur les autres logiciels sont datés du 2026-09-24 et relevés sur les sites des
  éditeurs**, pas écrits de mémoire. La date est sur la page, parce qu'une comparaison vieillit et
  que rien ne prévient quand elle devient fausse.

  Le passage le plus utile est le test que le lecteur peut faire lui-même : **couper le réseau et
  essayer de dicter**. Il tranche la question sans dépendre de ce qu'une page de présentation
  affirme, y compris la nôtre.

  ⚠️ **Le vocabulaire personnel y figure comme « prévu » et non comme disponible** : le code est
  écrit et commité, mais le dernier tag publié reste `v0.1.1`. Un correctif commité n'est pas un
  correctif livré, et l'annoncer ici l'aurait fait chercher dans le logiciel installé.

- **Signalement IndexNow**, `scripts/signaler-indexnow.py` et le fichier de clé servi à la racine.
  Le site n'était connu d'aucun moteur autrement que par la découverte spontanée : ce protocole
  prévient Bing, Yandex, Seznam et Naver qu'une page a changé, **sans demander aucun compte**, la
  preuve de propriété étant un fichier contenant la clé que le moteur va lire lui-même.

  ⚠️ **Les URL signalées sont dérivées de `sitemap.xml`**, jamais recopiées à la main : une liste
  tenue en double finit par diverger de celle qui fait autorité, et on signalerait alors une page
  disparue ou on en oublierait une neuve.

  ⛔ **Google n'utilise pas IndexNow**, et son ancien signalement de sitemap a été retiré en 2023 :
  il n'existe plus aucun chemin automatique vers lui. Le script le dit en toutes lettres en tête
  de fichier, pour que personne ne croie la question réglée pour autant.

### Corrigé

- **`llms.txt` disait de l'historique moins que ce que le site dit depuis le 2026-09-21** : il le
  décrivait comme « un fichier sur le disque » sans mentionner qu'il est désactivé par défaut.
  C'est le fichier écrit pour être lu par des machines, donc précisément celui qu'un moteur de
  réponse cite, et il portait la version la moins favorable d'un argument qui nous sert.

  ⚠️ **La correction du 2026-09-21 avait été passée page par page**, et ce fichier-là a été
  oublié parce qu'il n'est pas une page. Même famille que le repli branché écran par écran.

## [1.4.2] - 2026-09-21

### Corrigé

- ⛔ **Le site disait l'inverse de la vérité sur l'historique, et dans le sens qui nous dessert.**
  Il laissait entendre que Dictum conserve les dictées par défaut et qu'on peut choisir de n'en
  garder aucune. C'est l'inverse : **l'historique est désactivé par défaut** depuis le 2026-09-18,
  rien n'est écrit tant que l'utilisateur ne l'active pas, et remettre le réglage à zéro efface ce
  qui avait été gardé.

  Sur un public tenu au secret, c'est précisément la phrase qu'il lira deux fois, et la vérité est
  un bien meilleur argument que ce qui était écrit. Corrigé dans la carte de la section « comment
  ça marche », dans la réponse de la foire aux questions, dans son double au format `FAQPage`, et
  sur la page technique.

  ⚠️ **L'écart venait de moi et pas du logiciel** : j'avais présenté ce point comme une décision à
  prendre alors qu'il était tranché et implémenté depuis trois jours. Un test le garde désormais
  côté logiciel.

## [1.4.1] - 2026-09-21

### Corrigé

- ⛔ **Sur téléphone, cinq métiers sur six étaient décalés de 30 pixels vers la droite, et « Hors
  ligne » décalé sous « Zéro » qui ne l'était pas.** Signalé par painteau sur un vrai téléphone,
  pas vu en réduisant la fenêtre.

  La cause est un **sélecteur de fratrie dans une grille** : `.metier + .metier` et
  `.stat + .stat` posaient le retrait et le filet sur tout élément qui suit un autre, et un
  sélecteur de fratrie **ne sait rien des retours à la ligne d'une grille**. En une seule colonne,
  « suit un autre » vaut donc pour toutes les cartes sauf la première ; en deux colonnes, pour la
  première cellule de la deuxième ligne.

  ⚠️ **`nth-child` n'aurait pas sauvé le cas des métiers** : la grille est en `auto-fit`, donc le
  nombre de colonnes est implicite et aucune arithmétique ne peut le deviner.

  Le correctif **supprime le problème au lieu de le contourner** : un filet et un retrait à gauche
  de **chaque** cellule, la première comprise, comme painteau l'a proposé. Plus aucune cellule à
  traiter à part, et le même rendu de une à trois colonnes.

  ✅ **Vérifié par mesure plutôt qu'à l'œil** : sur une fenêtre de 393 pixels, les six métiers
  sont tous à 22 pixels du bord, et les chiffres retombent à `[22, 189, 22, 189]`, donc deux
  colonnes alignées.

- **Le héros réservait 168 pixels de marge haute sur téléphone**, soit près d'un tiers de l'écran
  avant le premier mot, alors que la barre fixe n'en occupe qu'une soixantaine. Ramené à 104, et
  la hauteur minimale retirée sur petit écran.

## [1.4.0] - 2026-09-21

### Corrigé

- ⛔ **Il n'y avait pas de cache buster, alors que c'est une règle du parc, et le défaut s'est
  manifesté pendant les essais mêmes.** `style.css` était servi avec `max-age=14400` sans empreinte
  dans son URL : le navigateur calculait encore `Segoe UI` pour le grand titre alors que la feuille
  **servie** déclarait bien Fraunces. J'ai d'abord cru à un déploiement en retard, puis à un cache
  de bord ; c'était le cache du navigateur, avec quatre heures d'avance sur la vérité.

  Le symptôme est le pire de sa famille : la page n'est pas cassée, elle est simplement **d'une
  autre époque**, et rien ne le signale.

  `scripts/poser-empreintes.py` pose désormais `style.css?v=<empreinte>` dans les quatre pages.
  ⚠️ **L'empreinte est DÉRIVÉE du contenu**, jamais un numéro écrit à la main : un numéro à côté du
  fichier qu'il décrit finit toujours par mentir, et un cache buster qui contient une version en
  clair la divulgue. Le cache de la feuille passe donc à un an et immuable, ce qui n'est
  acceptable **que** parce que l'URL change avec le contenu.

- **Un contrôle de sitemap qui se trompait a été corrigé avant d'être gardé** : il découpait l'URL
  sur le dernier `/` et rendait le nom de domaine pour la racine, donc il signalait `index` comme
  absent alors qu'il était déclaré. Un garde-fou faussement rouge finit ignoré, donc il valait
  mieux corriger la logique que le sitemap.

### Ajouté

- **Une CI, parce que les contrôles de ce dépôt existaient sans que rien ne les exécute.** Un
  garde-fou lancé à la main le jour où on l'écrit, puis plus jamais, ne dit rien : il donne
  seulement le sentiment d'être couvert. Quatre étapes, **chacune prouvée rouge** :

  | Contrôle | Ce qu'il attrape |
  |---|---|
  | Empreintes à jour | un CSS modifié sans reposer l'empreinte, donc un cache figé un an |
  | Classes et contrastes | une classe sans règle, et tout contraste sous le seuil AA |
  | JSON-LD et `@id` | une virgule de trop qui rend le schema invisible sans casser l'affichage |
  | Sitemap complet | une page servie mais non déclarée, donc inexistante pour un moteur |

## [1.3.0] - 2026-09-21

### Corrigé

- ⛔ **Le site avait ses propres polices, différentes de celles de l'application, et c'est une
  incohérence de marque que personne n'aurait dû introduire.** `dictum-desktop` embarque déjà
  **Fraunces**, **IBM Plex Sans** et **IBM Plex Mono** ; la passe de design précédente avait
  choisi Newsreader et Atkinson Hyperlegible pour le site seul. Une marque qui change de
  typographie entre sa page et son logiciel se contredit exactement là où elle demande qu'on lui
  fasse confiance.

  Les fichiers sont désormais pris **tels quels** dans `painteau/cdn`, que le commentaire de
  `src/styles/fontes.css` de l'application désigne comme la source commune au site, à
  l'application et à l'app iOS. ✅ **Les empreintes ont été comparées** : ce sont octet pour octet
  les mêmes. Les noms de rôles reprennent aussi ceux de l'application, `--titre`, `--corps`,
  `--mono`, pour qu'un lecteur qui compare les deux feuilles ne trouve pas deux vocabulaires.

  ⚠️ Un seul écart, délibéré : `font-display: swap` ici, `block` dans l'application. Une fenêtre
  d'application est convoquée pour quelques secondes et un échange de police en cours de lecture
  y gêne plus qu'un chargement local ; une page lue à distance doit au contraire s'afficher avant
  que la police arrive.

### Ajouté, après audit GEO mesuré

- **Une image de partage** (`partage.png`, 1200 x 630). ⚠️ **Elle manquait sur les trois pages** :
  un lien vers le site collé dans un courriel ou un message n'affichait aucune vignette, alors que
  c'est souvent la première chose qu'on voit du produit. Elle est générée depuis
  `scripts/carte-partage.html`, versionné : une image binaire dont le gabarit n'existe nulle part
  devient intouchable dès que la marque bouge.

- **`/details-techniques` dans le sitemap**, dont elle était absente depuis sa création. Elle
  répondait 200 et était donc invisible à tout robot qui se fie au sitemap : un contenu servi et
  non déclaré n'existe pas pour un moteur.

- **Du schema.org sur les pages secondaires**, qui n'en avaient aucun : `AboutPage` et
  `TechArticle`, plus un nœud **`WebSite`** sur l'accueil. ⚠️ Ce dernier corrige un défaut que
  j'avais introduit dans le même geste : les deux pages secondaires référençaient un `@id` de
  site que l'accueil ne définissait pas. Un contrôle des `@id` orphelins le vérifie désormais.

- **Le préchargement des deux polices variables**, sans quoi le grand titre s'affichait d'abord en
  Georgia puis sautait.

- **Un cache d'un an et immuable sur `/polices/*`**. Mesuré avant correction : Cloudflare Pages les
  servait avec `max-age=14400`, soit quatre heures, donc un visiteur qui revenait le lendemain les
  retéléchargeait. Et `font-src 'self'` déclaré explicitement dans la CSP, au lieu de reposer sur
  le repli de `default-src`.

## [1.2.0] - 2026-09-21

### Modifié

- **L'esthétique du site jouait contre son message, et c'était le vrai défaut.** Halos flous en
  dégradé, sections centrées, cartes arrondies partout : c'est le vocabulaire visuel d'une jeune
  pousse qui lève des fonds, et le public de ce site a précisément appris à s'en méfier. Un avocat
  fait confiance à un document composé, pas à une page qui brille.

  Direction retenue, **le mémo plutôt que la page d'atterrissage** : filets d'un pixel comme seule
  structure, sections numérotées comme des articles, alignement à gauche, et un serif éditorial
  réservé aux grandes déclarations.

  ⚠️ **La numérotation des sections vient du CSS** (`counter-increment`), pas du HTML : réordonner
  une section ne laisse donc aucun numéro faux derrière elle.

- **Les halos sont remplacés par un anneau, et ce n'est pas un choix décoratif.** Là où un halo
  flou **diffuse**, un cercle **enferme**, ce qui est exactement le propos du produit. Ce sont les
  deux cercles concentriques du logo, agrandis derrière le titre, et l'aperçu de l'application est
  désormais **calé au centre de l'anneau** : l'application est littéralement enfermée dans le
  cercle.

  ⚠️ Cela a imposé de passer les dimensions de l'anneau **en pixels avec un centre déclaré en
  variable** : en unités relatives, le centre se déplaçait avec la largeur de la fenêtre et rien
  ne restait calé dessus.

- **Deux polices, auto-hébergées, et aucune n'est un choix par défaut.** La CSP du site est
  `default-src 'self'` et ne sera pas assouplie, donc les fichiers sont dans le dépôt, avec leur
  licence OFL. 148 Ko au total.

  **Atkinson Hyperlegible** pour le texte : elle est dessinée par le Braille Institute pour être
  lisible par des personnes malvoyantes, avec des lettres volontairement impossibles à confondre.
  Sur un produit dont l'argument est la confiance et dont l'accessibilité est une exigence dure,
  la police faite pour être lue n'est pas un effet de style.

  **Newsreader** pour les titres et les chiffres, prise à sa **taille optique 72pt**, celle qui
  est dessinée pour le grand corps. ⚠️ La variable de la même famille pesait 210 Ko pour un usage
  limité aux titres : la statique 72pt fait le même travail en 50 Ko. Et le serif garde sa force
  parce qu'il est rare, le sans conservant tout le fonctionnel.

- **Les chiffres du bandeau passent en grille à colonnes égales** : en `flex`, « Hors ligne »
  repoussait ses voisines et les filets verticaux ne tombaient plus au même pas.

### Ajouté

- **Un grain de papier** en turbulence SVG `data:` à très basse opacité, qui enlève l'aspect
  numérique plat sans se voir, et sans une requête réseau de plus.

- **Le balayage des couleurs de texte écrites en dur** dans `scripts/verifier-site.py`. Les paires
  nommées à la main ne couvrent que ce qu'on a pensé à nommer ; ce balayage éprouve chaque couleur
  littérale de la feuille contre le pire fond du site. Il a immédiatement trouvé les deux que
  cette passe venait d'introduire.

  ⛔ **Et il a d'abord menti, pour la raison exacte que la règle du parc annonce.** Sa ligne de
  regex est passée par un heredoc de shell, où le `\b` est devenu un **caractère de retour
  arrière invisible** : le fichier s'affichait normalement et le balayage annonçait « aucune
  couleur en dur » alors qu'il y en avait deux. Un garde-fou qui mentait, attrapé par
  `verifier-caracteres-de-controle.py`, qui a nommé le caractère, sa position et le remède. Du
  contenu de fichier ne passe jamais par un heredoc.

- **Un repli explicite quand le JavaScript ne tourne pas** (`@media (scripting: none)`) et sous
  `prefers-reduced-motion`. ⚠️ Sans la remise à `opacity: 1`, quelqu'un qui demande moins
  d'animation voyait une page **vide** : les révélations au défilement laissaient tout invisible.


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

