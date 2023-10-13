## Contexte et introduction

<br>

**Utilisez les bases de Python pour l'analyse de marché** est le 2ème projet de [l'école OpenClassroom](https://openclassrooms.com/fr). L'objectif est de travailler sur le processus d'extraction de données ETL **Extract Transform Load**. Les données à scraper sont sur le site [Book to scrap](http://books.toscrape.com/index.html).

<br>

<br>

# Scraping et Organisation
<br>

## Arborescence du projet

Trouvez ci-dessous l'organisation du projet.
<br>

```bash
.
├── __init__.py                    # __init__ file
├── book.py                        # Défini la class Book qui recense toutes les fonctions nécessaires à l'extraction de données ciblées pour un livre.
├── csv_books.py                   # Transcrit la donnée téléchargée dans un fichier au format csv. 
├── data                           # Dossier data où l'on peut retrouver toute la donnée extraite et téléchargée après l'execution du programme.
│   └── category                   # Chaque dossier par catégories contient un csv et des images.
│           └── catagory.csv
│           └── book.jpg
└── requirements.txt               # répertorie toutes les librairies et modules nécessaires à l'exécution du programme 
```
<br>

## Les données à extraire

<br>

La consigne est d'extraire les données suivantes pour chaque livres :
<br>

    - title
    - universal_product_code(upc)
    - product_page_url
    - price_excluding_tax
    - price_including_tax
    - availablility
    - product_description
    - category
    - review_rating
    - image_url
    - image_path

<br>

# Lancement du projet

<br>

Pour lancer le programme veuillez suivre les étapes suivantes :

<br>

Installer Python. Ouvrir le terminal, se placer dans le dossier de votre choix et cloner le projet dans ce dossier:

```bash
git clone https://github.com/Jbguerin13/Python-basics-for-market-analysis.git
```

Se placer dans le dossier **projet_web-scraping**, puis créer un nouvel environnement virtuel et l'activer :

```bash
python -m venv nom_env
source nom_env/bin/activate
```

Il ne reste plus qu'à installer les dépendances requises pour setup le programme :

```bash
pip install -r requirements.txt
```

Créer un dossier nommé data dans le dossier du projet et lancer le programme en appelant la commande suivante :

```bash
python main.py
```

<br>

# Récupération de la donnée

Attendez quelques minutes que l'ensemble des données soit téléchargée, puis récupérez là dans le dossier data que vous auriez préalablement créer.
Un CSV contenant toutes les informations demandées au sujet d'un livre, accompagne chaque dossier correspondant aux catégories d'ouvrages disponibles.