# Exercice Python - Manipulation de fichiers CSV

> Ces exercices sont destinés à un public découvrant Python, mais ayant pu apprendre les bases de Python à travers différents cours. Cet exercice permet de pratiquer celles ci.

Vous trouverez ci-dessous des fichiers CSV dans le dossier `/data`.
A travers les différents exercices, vous serez amené à manipuler ces fichiers.
Par simplicité, vous trouverez un fichier `main.py` pour réaliser les exercices. Au fil des exercices, vous serez amenés à créer vos propres fichiers et dossiers.

## Exercice 1 - Manipulation de fichiers

### Appel de fonction et affichage
Voici le code python pour récupérer un tableau avec l'ensemble des noms de fichier dans un dossier (donné en paramètre) :

```python
import os

def get_file_names(folder_path):
    return os.listdir(folder_path)
```

Copiez cette fonction dans le fichier `main.py` et appelez la fonction avec le dossier `/data`. Affichez le résultat.

<details>
<summary>Aide</summary>

```python
files = get_file_names('data')
```
</details>

### Verifier l'existence d'un fichier

1. Au début du programme, demandez à l'utilisateur de rentrer un nom de fichier. Vérifiez si le fichier existe dans le dossier `/data`. Si le fichier n'existe pas, afficher un message d'erreur et demander à l'utilisateur de rentrer un nouveau nom de fichier.
2. C'est ennuyant l'utilisateur doit rentrer l'extension du fichier. Modifier le code pour que l'utilisateur rentre uniquement le nom du fichier. Si plusieurs fichiers existent avec le même nom, afficher tous les fichiers existants.
<details>
<summary>Aide</summary>

Pour récupérer la liste des fichiers ayant le nom donnée:

1. Il vous faudra boucler sur la liste des fichiers `for`.
2. Il vous faudra découper le nom du ficher, pour récupérer son nom sans l'extension `.split()`. https://docs.python.org/3.3/library/stdtypes.html#str.split
3. Si le nom du fichier est égal au nom donné, ajouter le fichier à la liste des fichiers trouvés (`.append(xxx)`)
</details>

<details>
<summary>Super Aide</summary>

```python
def find_matching_files(files, name):
    matches = []
    for f in files:
        if f.split('.')[0] == name:
            matches.append(f)
    return matches
```
</details>

### Filtrage des csv
Avant de demander à l'utilisateur de rentrer un nom de fichier. Affichez la liste des fichiers csv présent dans le dossier `/data`.
(vous pouvez utiliser la fonction `endswith` pour savoir si un nom de fichier termine par 'csv', https://docs.python.org/3/library/stdtypes.html#str.endswith)

## Exercice 2 - Lecture de fichier csv

### Lecture d'un fichier
Au début du programme, afficher la liste des fichiers csv disponibles. Demander à l'utilisateur de rentrer un nom de fichier (sans l'extension). Si le fichier csv n'existe pas, afficher un message d'erreur et demander à l'utilisateur de rentrer un nouveau nom de fichier.

Si le fichier existe, lire le fichier et afficher son contenu. Chercher sur internet comment lire un fichier csv avec python.

Après avoir chercher sur internet, vous pourrez trouver quelques explications [ici](./explications/read_files_flags.md)

> Pour aller plus loin, quoi faire si on trouve plusieurs fichiers csv avec le même nom ? C'est hypothétiquement impossible, mais il nous faut quand même prendre en compte cette possibilité. Si cela arrive c'est une erreur. Donc nous pouvons lancer une erreur. `raise ValueError("Multiple csv files found")`

<details>
<summary>Aide</summary>

La documentation officielle: https://pythonspot.com/read-file/
Un tuto en francais: https://python.doctor/page-lire-ecrire-creer-fichier-python

Il vous faudra utiliser la fonction `open` et la méthode `readlines`.
</details>

### Comptage de ligne
Vous pouvez supprimer le `print` qui affiche le contenu du fichier dans la console.
Maintenant, comptez le nombre de ligne dans le fichier. Et afficher le résultat à l'utilisateur.

### Afficher les entêtes
Les entêtes dans un fichier csv, sont forcément les premières lignes du fichier. Afficher un tableau avec les entêtes du fichier.

> Pensez à bien découper la première ligne du fichier avec la fonction `split`

> Attention la derniere colonne du fichier peut contenir un caractère de retour à la ligne `\n`. Il faut donc enlever ce caractère avec la fonction `replace`.

### Création du tableau
Parfait, maintenant nous allons créer un tableau à double entrée avec les entêtes du fichier.
Un tableau à double entrée est un tableau de tableau:
```python
tableau = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
Comme vous pouvez le voir, chaque ligne du tableau est elle même un tableau.

Pour chaque ligne du fichier, découper la ligne avec la fonction `split` et ajouter les valeurs dans le tableau.

### Amélioration du tableau
Maintenant, nous allons améliorer le tableau, un tableau de tableau ce n'est pas très pratique pour savoir quelle colonne est quelle colonne, il faut toujours se référer à l'entête du fichier.

Donc nous allons créer un tableau de dictionnaire, exemple:
```python
tableau = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

<details>
<summary>Aide</summary>

Pour boucler sur un tableau, et avoir la valeur de chaque ligne et l'index de la ligne, il faut utiliser la fonction `enumerate`.

```python
tableau = ["foo", "bar", "baz"]
for i, value in enumerate(tableau):
    print(i, value)

# 0 foo
# 1 bar
# 2 baz
```

</details>

### Utilisation de la librairie `csv`
C'est très bien nous avons codé un parser de fichier csv, mais il existe une librairie qui fait ca très bien.
La documentation officielle: https://docs.python.org/3/library/csv.html

Lisez la documentation et remplacer votre qui créer un tableau de dictionnaire par la librairie `csv`.

> Attention, il vous faudra enlever tout votre code precedent, nottament `.readlines()`. Sinon la librairie `csv` risque de vous retourner que des tableaux vide. Cela vient du fonctionnement de la lecture des fichiers en python [explications](./explications/read_file_cursor.md)

<details>
<summary>Aide</summary>
Regardez du coté de la fonction `csv.DictReader`.

> Si vous essayez d'afficher le résultat, vous verrez surement `<csv.DictReader object at 0x104d3b820>`.
> Pour afficher le résultat, il faut convertir le résultat en liste avec la fonction `list`: `print(list(table))`
</details>

## Exercice 3 - Ecriture de fichier

### Creation d'un fichier

Nous allons repartir d'un fichier propre (ne supprimez pas les anciens, nous en aurons besoin plus tard).

Dans ce fichier, essayez de créer un fichier 'test.txt' dans parsed_data, avec le texte 'Hello World'. Si besoin, allez vous renseigner sur internet.

### Ecriture de fichier csv

Dans votre fichier, ajouter ce tableau de dictionnaire:
```python
users = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

Essayer maintenant de créer un nouveau fichier csv avec ce tableau.

<details>
<summary>Aide</summary>

Pour écrire un fichier csv, il faut d'abord écrire les entêtes, puis les lignes.

Pour écrire les entêtes, il faut découper les clés du premier dictionnaire avec la fonction `keys` et les ajouter à la ligne avec la fonction `join`.

Pour écrire les lignes, il faut récupérer les valeurs de chaque utilisateur, en les mettant dans le même ordre que les entêtes. Puis les ajouter à la ligne avec la fonction `join`.

Penser à bien ajouter le caractère de retour à la ligne `\n` à la fin de chaque ligne.
</details>

### Utilisation de la librairie `csv`
Comme d'habitude, il existe une librairie qui fait ca très bien. Utilisez la librairie `csv` pour écrire le fichier csv des utilisateurs.

<details>
<summary>Aide</summary>

Regardez du coté de la fonction `csv.DictWriter`. Et les méthodes `writeheader` et `writerows`.
</details>


## Exercice 4 - Re-écriture d'une colonne
Maintenant que l'on sait lire et écrire des fichiers, nous allons pouvoir les manipuler.

> À partir de maintenant, les exercices seront moins détaillé et accompagné d'une petite mise en contexte.

Vous êtes un developpeur pour une entreprise de vente en ligne. Vous êtes en train de changer de logiciel de comptabilité. Vous pouvez passer les informations de l'ancien logiciel vers le nouveau en utilisant des fichiers CSV. Mais il y a un problème avec le fichier `products.csv`. En effet la valeur de la colonne `archived` est noté `VRAI` ou `FAUX`. Mais le nouveau logiciel ne supporte que `TRUE` ou `FALSE`.
Donc ouvrez le fichier avec python, modifier la valeur de la colonne `archived` en `TRUE` ou `FALSE` et écrivez le nouveau fichier dans le dossier `parsed_data`.

## Exercice 5 - Ajouter la monnaie en fonction du pays

Toujours pour votre nouveau logiciel de comptabilité, il vous demande obligatoirement une devise (EUR, USD, GBP, etc...) pour chaque utilisateur.

Actuellement, dans le fichier `users.csv` vous avez le pays de l'utilisateur, utilisé le pour ajouter une colonne `currency`, avec les valeurs suivantes:
- FR, ES: EUR
- US: USD
- UK: GBP

## Exercice 6 - Faire la somme des achats par user

Votre collègue commercial aimerait faire une campagne pour remercier vos meilleurs clients. Pour cela il vous demande la somme totale des achats de chaque utilisateur, et de lui fournir les emails et noms des 3 meilleurs clients.

Faite un script python qui, à l'aides des fichiers `users.csv` et `invoices.csv` et `orders.csv`, va vous afficher dans la console les emails et noms des 3 meilleurs clients, avec la somme totale de leurs achats.

<details>
<summary>Aide</summary>

Pour faire la somme des achats de chaque utilisateur, il faut lire le fichier `orders.csv` et récupérer le prix de chaque `invoice_id`. Puis regrouper chaque `invoice_id` par `user_id`, faire la somme globale et trouver les 3 plus élevé (pour trouver le 3 plus élevé, il faut trier les valeurs et prendre les 3 dernières (en cas d'ordre croissant), regardez du coté de la fonction `sorted`) https://docs.python.org/3/howto/sorting.html.

</details>

## Exercie 7 - Créer son propre logiciel de comptabilité POO

Finalement personne n'aime votre nouveau logiciel de comptabilité, vous avez donc décidez de créer le votre.

Nous allons créer une version simplifiée d'un magasin en ligne de commande. Celui ci sera capable de lire les fichiers csv, de les modifier et de re-sauvergarder le tout dans des fichiers csv.

> Le code produit sera une approche très basique et simplifiée, mais il permettra de mettre en pratique la programmation orienté objet.

Nous allons créer 4 classes, une pour chaque fichier csv:
- `User`
- `Product`
- `Order`
- `Invoice`

Chacune de ces classes instanciera les headers des fichers CSV en tant qu'attribut (example: user possedera les attribut `id`, `lastname`, `firstname`, `email`, etc...). Dans le cas des `Orders`, au lieu de stocker un identifiant d'un autre objet, nous stockerons directement son instance. Exemple: au lieu de stocker un `user_id`, nous stockerons directement un objet `User`.

Chaque classe possèdera 3 méthodes static pour intéragir avec les fichier CSV:
- `get`: qui va directement récupérer l'instance de la classe en fonction de son id, et retourner l'instance.
- `load` qui va lire le fichier csv et retourner une liste d'instances de la classe.
- `save` qui va écrire les instances dans le fichier csv.

> Pour que cela fonctionne, vous devrez avoir un attribut static `instances` qui stockera toutes les instances de la classe.

<details>
<summary>Tips</summary>
La fonction `load` de `Order` devra utiliser les méthodes `get` de `Invoice` et `User`.
</details>

Le programme demarre en déclenchant la fonction `load` de toute les classes.

Ensuite, créer un menu en console qui permettra de créer:
- créer un user
- créer un produit
- créer une commande (qui permet de renseigner plusieurs produits et quantités)
- sauvegarder les données



> Pour centraliser la logique d'interaction avec les fichiers csv, il est conseillé de créer une classe mère abstraite `CsvModel` qui contiendra la logique commune du traitement des fichiers csv.

> Pour parser les dates, il est conseillé d'utiliser la librairie `datetime` https://docs.python.org/3/library/datetime.html, nottament la fonction `strptime`.

> Essayer de faire en sorte que le programme ne crash pas en cas d'erreur d'une saisie utilisateur.

### Pour aller plus loin
- Ajouter une commande qui permet de récupérer les N plus gros acheteurs (vous aurez peut être besoin de créer plus d'associations entre les classes)
- Ajouter des filtres sur la creation d'instance (exemple: le mail doit être valide, le prix doit être positif, etc...)
- Ajouter des commandes supplémentaires (exemple: afficher tous les produits, afficher tous les utilisateurs, etc...)
