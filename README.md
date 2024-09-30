## Urban Weather Generator
>dossier pour comprendre et utiliser l'outil UWG (Urban Weather Generator).

**Urban Weather Generator** est une application pour modéliser les *îlots de chaleur urbains* (ICU). Il s'agit à l'origine du projet de thèse de Bruno Bueno Unzeta (2007), implémenté en Matlab. L'outil proposé par les développeurs derrière [Ladybug-tools](https://github.com/ladybug-tools) est une traduction Python de l'outil Matlab (qui depuis sa création, a été modifié et amélioré par d'autres chercheurs/développeurs). Pour en savoir plus sur [Ladybug Tools](https://www.ladybug.tools/) (il y a beaucoup d'outils qui pourrait intéresser INEX !)

### Contenu du dossier
---
- `resources` :
    - `SGP_Singapore.486980_IWEC.epw` : fichier météo (pour le tutoriel)
- `scripts`
    - `uwg_tutorial.ipynb` : notebook tutoriel (en anglais, me demandez pas pourquoi) pour l'utilisation du module `uwg` et ouvrir des fichiers `EPW` en Python ;
    - `run_uwg.py` : script pour lancer simulation UWG à partir d'un fichier EPW.
- `UWG_thesis.pdf` : An Urban Weather Generator Coupling a Building Simulation Program with an Urban Canopy Model, Bruno Bueno Unzeta, 2007.

### Installation de Python
---
Afin d'utiliser le script `run_uwg.py`, il faut télécharger [Python](https://www.python.org/downloads/). Suivre les indications données par la fenêtre (il faut que `python.exe` soit ajouté à la variable d'environnement `PATH`, et installer la commande `pip`, cette dernière permet d'installer des modules Python depuis le terminal en ligne de commande).