# Pràctica Kaggle APC UAB 2021-22
### Nom: Alberto Romero Cabezas
### DATASET: Android Permission Dataset
### URL: [kaggle] https://www.kaggle.com/saurabhshahane/android-permission-dataset

## Resum
El dataset conté una serie d'aplicacions per dispositius Android especificant els permisos que es demana al usuari per accedir a funcionalitat clau de
l'smartphone, classificant les apps com a possibles malware o aplicacions benignes, es a dir que no contenet cap activitat sospitosa. A més, inclou el preu
de l'app, si aquesta no es de franc, la valoració dels usuaris, la categoria o tipus d'aplicació i el paquet instalador que utilitza.
Tenim 29999 dades amb 184 atributs. La majoria d'atributs són categorics, per exemple, a l'atribut corresponent a un permís, aquesta pot ser o 1 (es demana a l'usuari)
o 0 (no es demana), o la categoria de l'aplicació, es a dir, si es un app de negoci o de jocs. Per un altre banda, com atributs numèrics només trobem 3: Rating,
Number of ratings i Price.

### Objectius del dataset
L'objectiu principal d'aquesta dataset es poder predir si una aplicació pot ser maliciós, és a dir que pot tenir un comportament inadequat en el notres telèfon mòbil,
per un altre banda, és segur instal·lar-ho i utilitzar en el nostre dispositiu.

## Experiments
Durant aquesta pràctica hem realitzat diferents experiments que comportaba al analisis dels atributs del dataset:
    1) Percentatge d'apliacions benignes i maliciosos: Calculem i comparem la quantitat d'aplicacions que tenen un comportament maligne al nostre dispositiu i quins no.
    2) Correlació dels atributs: És calcula la correlació de algunes variables destacades per tal de saber quina realció tene amb la variable objectiva "Class".
    3) Diagrama de caixes:
        3.1) Nº de permisos perillosos: Sabes quins són els quartils de permisos perillosos i els seus outliers tant en les aplicacions benignes com malicioses.
        3.2) Nº de permisos segurs: Sabes quins són els quartils de permisos segurs i els seus outliers tant en les aplicacions benignes com malicioses.
        3.3) Ratings: Comprobar el quartils dels ratings dels usuaris i els seus outliers tant en les aplicacions benignes com malicioses.
    4) Diagrama de barres:
        4.1) Aplicacions benignes per cada catgeoria: Mostra del numero de aplicacions segures per cada categoria.
        4.2) Aplicacions malicioses per cada catgeoria: Mostra del numero de aplicacions no segures per cada categoria.
        4.3) Comparció de preus: Mostra del preu en funció de si l'app és benigne o maliciós.
    5) Nº d'apps benignes per paquet
    6) Nº d'apps malicioses per paquet

### Preprocessat
Pel que fa al preporcessat s'han realitzat dues accions:
    1) Transformar els atributs categòrics "Category" i "Package" en valors enters per tal de poder fer els experiments d'anàlisi i en cas de que sigui necessari,
       utilitzar-les com variables per predir la classe d'una aplicació.
    2) Eliminar aquelles mostres que continguin variables buides.
    3) S'ha fet un Coss-Validation en el que es particiona les dades en dues parts, un d'entrenament, que correspon a un 80% d'aquestes, i un de prova, que correspon
       al 20% restant.
    
### Model
Els models que s'han utilitzat i comporbat han sigut: 
    1) Gradient Boosting Classifier
    2) Ridge Classifier
    3) Gaussian Naive Bayes
    4) Random Forest Classifier
    5) Regressió Logística
 
 Per tal de veure els resultats s'han genera per cada model predictiu un "Classification Report", que conté els resultats del "Precision", "Recall" i el "f1-score",
 i una matriu de confusió que indica els falsos benignes i maliciosos, a més del benignes i maliciosos positius.
 
 A continuació, es pot veure els resultats que s'han obtenit per cada model:

| Model | precision | recall | f1-score | True Beniges | Treu Maliciós | False Beniges | False Maliciós |
| Gradient Boosting Classifier | 0.76 | 0.77 | 0.76 | 1453 | 3110 | 766 | 519 |
| Ridge Classifier | 0.60 | 0.57 | 0.56 | 521 | 3367 | 509 | 1451 |
| Gaussian Naive Bayes | 0.72 | 0.70 | 0.60 | 1931 | 1600 | 2276 | 41 |
| Random Forest Classifier | 0.72 | 0.72 | 0.72 | 1228 | 3147 | 729 | 744 |
| Regressió Logística | 0.66 | 0.65 | 0.66 | 1017 | 3070 | 806 | 955 |

## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda:
```python demo/demo.py```

## Conclusions
El millor model que s'ha aconseguit ha estat el "Gradient Boosting Classifier", ja que en el que respecta als valors de precision i recall, és el model amb millors 
resultats (precision = 0.76, recall = 0.77). Y pel que fa a la matriu de confunsió, podem trobar que hi ha un equilibri entre ells, es a dir, que podem descartar 
l'aparició de overfitting.

## Idees per treballar en un futur
Crec que seria interesant indagar més en alguns dels atributs del dataset, ja que pot ser molt interessant el poder detectar aplicacions que poden ser perjudicials per el
nostre smartphone amb sistema operatiu Android, sobretot per els programas d'antivirus com Avast o AVG.
