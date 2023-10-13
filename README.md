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
├── book.py                        # Define class Book where we can find all the methods used to scrap the data from each books
├── csv_books.py                   # Write done the data into  
├── data                           # Data folder where you can find all the categories folders (contain csv and image)
│   └── category                   # Each folder by categories contain csv and image files
│           └── catagory.csv
│           └── book.jpg
├── requirements.txt               # all the dependencies we need to run the package
└── setup.py                       # package installer
```
<br>

## Les données à extraire

<br>

La consigne est d'extraire les données suivante pour chaque livres :
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

Pour lancer le programme vous devrez suivre les étapes suivantes :

<br>

Commencez tout d'abord par installer Python. Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:

```bash
git clone 
```

Placez vous dans le dossier **projet_web-scraping**, puis créez un nouvel environnement virtuel et activez le :

```bash
python -m venv nom_env
source nom_env/bin/activate
```

Il ne reste plus qu'à installer les packages requis:

```bash
pip install -r requirements.txt
```

Vous pouvez ensuite lancer le programme en appelant la commande suivante :
```bash
python main.py
```

<br>

# 3️⃣ Make and run the models

## CNN Model - initialize, compile and train

<br>

A conventionnal CNN model is initialized using the `initialize_cnn` method.
Three **Conv2D** layers followed by three **MaxPooling2D** layers are used before the **Flatten** and **Dense** layers.
The output layer uses the softmax activation function to predict 100 probabilities.

The model is compiled using `compile_cnn`. A simple **Adam** optimizer, a **sparse categorical crossentropy** loss function are used. The **accuracy** metrics is monitored.

```python
#Initialize a CNN Model

model = Sequential()

    model.add(Conv2D(16, (3,3), activation='relu', input_shape=(28,28,1)))
    model.add(MaxPooling2D((2,2)))

    model.add(Conv2D(32, (3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D((2,2)))

    model.add(Conv2D(64, (3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D((2,2)))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    #model.add(Dropout(0.4))
    model.add(Dense(num_classes, activation = 'softmax'))

#Compile

model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])
```
<br>

The final accuracy lies around 80% which is sufficient for categorizing sketches.

Here is a 3D visualization of the CNN model

<br>

![visualkeras CNN layers](images/visualkeras_cnn-layer.png)

<br>

### CNN Modelisation results

<br>

Here is the final confusion matrix and the final classification report.

<br>

![plot confusion matrix of CNN](images/confusion-matrix_cnn.png)

<br>

![sample of classification report of CNN](images/sample_classif-report_cnn.png)

<br>

## Activation map

<br>

The activation map shows how the 16 filters of the first convolution layer specialized during training.
3 examples from 3 categories of sketches 🐱 🐷 🐸 are represented bellow.
<br>

![Sample of data encoded 🐱 🐷 🐸](images/bitmap_28*28.png)

<br>

![Cat picture with the first convolution layer effect](images/layer1_part1.png)
![](images/layer1_part2.png)

<br>

## RNN Model - initialize, compile and train

<br>

The RNN model is initialized using the `initialize_rnn_tfrecords` method.

One **Masking** layer followed by two **LSTM** layers are used before the **Dense** layer.
The output layers uses the softmax activation function to predict 100 probabilities.

The RNN model is compiled as the same way than Like the CNN model.

<br>

```python
#Initialize a RNN Model

model = Sequential()

    model.add(layers.Masking(mask_value=1000, input_shape=(1920,3)))
    model.add(layers.LSTM(units = 20, activation= 'tanh', return_sequences= True))
    model.add(layers.LSTM(units = 20, activation= 'tanh', return_sequences= False))

    model.add(Dense(50, activation='relu'))
    model.add(Dense(num_classes, activation = 'softmax'))
```

<br>

The final accuracy for the RNN model lies around 75% which is sufficient for categorizing sketches.

<br>

### RNN Modelisation results

<br>

Here is the final confusion matrix and the final classification report.

<br>

![plot confusion matrix of RNN](images/confusion-matrix_rnn.png)

<br>

![sample of classification report of RNN](images/sample_classif-report_rnn.png)






------Présentation-------

Ce programme permet d'effectuer le scraping les données du site internet book to scrap. Ces données sont les suivantes

['product_page_url',
                  'universal_product_code(upc)',
                  'title',
                  'price_excluding_tax',
                  'price_including_tax',
                  'number_available',
                  'product_description',
                  'category',
                  'review_rating',
                  'image_url']

Au lancement du programme, vous retouverez toutes les données scrapées dans le dossier data. Les données seront alors classées par catégorie de livres.

-------------------Installation et run du programme-------------------

Etape 1

Lancer le terminal
Générer un environnement virtuel spécifique à ce programme

Etape 2

installer les dependencies

Etape 3 

lancer main.py