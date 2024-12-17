# Exercice Python - Manipulation de fichiers CSV

> Ces exercices sont destinés à un public découvrant Python, mais ayant déjà appris les bases du langage à travers différents cours. Ils permettront de mettre en pratique et de consolider ces connaissances.

Vous trouverez ci-dessous des fichiers CSV dans le dossier `/data`.
À travers les différents exercices, vous serez amené à manipuler ces fichiers.
Pour plus de simplicité, vous trouverez un fichier `main.py` pour réaliser les exercices. Au fil des exercices, vous serez amené à créer vos propres fichiers et dossiers.

## Exercice 1 - Manipulation de fichiers

### Appel de fonction et affichage
Voici le code Python pour récupérer un tableau avec l'ensemble des noms de fichiers dans un dossier (donné en paramètre) :

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

### Vérifier l'existence d'un fichier

1. Au début du programme, demandez à l'utilisateur de saisir un nom de fichier. Vérifiez si le fichier existe dans le dossier `/data`. Si le fichier n'existe pas, affichez un message d'erreur et demandez à l'utilisateur de saisir un nouveau nom de fichier.
2. Il est fastidieux que l'utilisateur doive saisir l'extension du fichier. Modifiez le code pour que l'utilisateur n'entre que le nom du fichier. Si plusieurs fichiers existent avec le même nom, affichez tous les fichiers existants.

<details>
<summary>Aide</summary>

Pour récupérer la liste des fichiers portant le nom donné :

1. Utilisez une boucle `for` pour parcourir la liste des fichiers.
2. Découpez le nom du fichier pour récupérer son nom sans l'extension avec `.split()`. (https://docs.python.org/3.3/library/stdtypes.html#str.split)
3. Si le nom du fichier correspond au nom donné, ajoutez-le à la liste des fichiers trouvés avec `.append(xxx)`.
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

### Filtrage des CSV
Avant de demander à l'utilisateur de saisir un nom de fichier, affichez la liste des fichiers CSV présents dans le dossier `/data`.
(Vous pouvez utiliser la méthode `endswith` pour vérifier si un nom de fichier se termine par 'csv', https://docs.python.org/3/library/stdtypes.html#str.endswith)

## Exercice 2 - Lecture de fichier CSV

### Lecture d'un fichier
Au début du programme, affichez la liste des fichiers CSV disponibles. Demandez à l'utilisateur de saisir un nom de fichier (sans l'extension). Si le fichier CSV n'existe pas, affichez un message d'erreur et demandez à l'utilisateur de saisir un nouveau nom de fichier.

Si le fichier existe, lisez le fichier et affichez son contenu. Recherchez sur internet comment lire un fichier CSV avec Python.

Après avoir effectué des recherches, vous pourrez trouver quelques explications [ici](./explications/read_files_flags_fr.md)

> Pour aller plus loin, que faire si l'on trouve plusieurs fichiers CSV avec le même nom ? C'est hypothétiquement impossible, mais il nous faut quand même prendre en compte cette possibilité. Si cela arrive, c'est une erreur. Nous pouvons donc lancer une erreur : `raise ValueError("Multiple csv files found")`

<details>
<summary>Aide</summary>

La documentation officielle : https://pythonspot.com/read-file/
Un tutoriel en français : https://python.doctor/page-lire-ecrire-creer-fichier-python

Vous devrez utiliser la fonction `open` et la méthode `readlines`.
</details>

### Comptage de lignes
Vous pouvez supprimer le `print` qui affiche le contenu du fichier dans la console.
Maintenant, comptez le nombre de lignes dans le fichier et affichez le résultat à l'utilisateur.

### Afficher les en-têtes
Les en-têtes dans un fichier CSV sont forcément les premières lignes du fichier. Affichez un tableau avec les en-têtes du fichier.

> Pensez à bien découper la première ligne du fichier avec la fonction `split`.

> Attention, la dernière colonne du fichier peut contenir un caractère de retour à la ligne `\n`. Il faut donc enlever ce caractère avec la fonction `replace`.

### Création du tableau
Parfait, maintenant nous allons créer un tableau à double entrée avec les en-têtes du fichier.
Un tableau à double entrée est un tableau de tableaux :
```python
tableau = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
Comme vous pouvez le voir, chaque ligne du tableau est elle-même un tableau.

Pour chaque ligne du fichier, découpez la ligne avec la fonction `split` et ajoutez les valeurs dans le tableau.

### Amélioration du tableau
Maintenant, nous allons améliorer le tableau. Un tableau de tableaux n'est pas très pratique pour identifier chaque colonne, car il faut toujours se référer à l'en-tête du fichier.

Nous allons donc créer un tableau de dictionnaires, par exemple :
```python
tableau = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

<details>
<summary>Aide</summary>

Pour parcourir un tableau et obtenir la valeur de chaque ligne ainsi que son index, utilisez la fonction `enumerate`.

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
C'est très bien, nous avons codé un parseur de fichier CSV, mais il existe une bibliothèque qui le fait très bien.
La documentation officielle : https://docs.python.org/3/library/csv.html

Lisez la documentation et remplacez votre code qui crée un tableau de dictionnaires par la bibliothèque `csv`.

> Attention, il vous faudra enlever tout votre code précédent, notamment `.readlines()`. Sinon, la bibliothèque `csv` risque de vous retourner des tableaux vides. Cela vient du fonctionnement de la lecture des fichiers en Python [explications](./explications/read_file_cursor_fr.md)

<details>
<summary>Aide</summary>
Regardez du côté de la fonction `csv.DictReader`.

> Si vous essayez d'afficher le résultat, vous verrez sûrement `<csv.DictReader object at 0x104d3b820>`.
> Pour afficher le résultat, il faut convertir le résultat en liste avec la fonction `list` : `print(list(table))`
</details>

## Exercice 3 - Écriture de fichier

### Création d'un fichier

Nous allons repartir d'un fichier propre (ne supprimez pas les anciens, nous en aurons besoin plus tard).

Dans ce fichier, essayez de créer un fichier 'test.txt' dans le dossier parsed_data, avec le texte 'Hello World'. Si besoin, renseignez-vous sur internet.

### Écriture de fichier CSV

Dans votre fichier, ajoutez ce tableau de dictionnaires :
```python
users = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'London'},
    {'name': 'Mike', 'age': 32, 'city': 'San Francisco'}
]
```

Essayez maintenant de créer un nouveau fichier CSV avec ce tableau.

<details>
<summary>Aide</summary>

Pour écrire un fichier CSV, il faut d'abord écrire les en-têtes, puis les lignes.

Pour écrire les en-têtes, découpez les clés du premier dictionnaire avec la méthode `keys` et ajoutez-les à la ligne avec la fonction `join`.

Pour écrire les lignes, récupérez les valeurs de chaque utilisateur, en les mettant dans le même ordre que les en-têtes. Puis ajoutez-les à la ligne avec la fonction `join`.

Pensez à bien ajouter le caractère de retour à la ligne `\n` à la fin de chaque ligne.
</details>

### Utilisation de la librairie `csv`
Comme d'habitude, il existe une bibliothèque qui fait cela très bien. Utilisez la bibliothèque `csv` pour écrire le fichier CSV des utilisateurs.

<details>
<summary>Aide</summary>

Regardez du côté de la fonction `csv.DictWriter`. Utilisez les méthodes `writeheader` et `writerows`.
</details>

## Exercice 4 - Réécriture d'une colonne
Maintenant que nous savons lire et écrire des fichiers, nous allons pouvoir les manipuler.

> À partir de maintenant, les exercices seront moins détaillés et accompagnés d'une petite mise en contexte.

Vous êtes un développeur pour une entreprise de vente en ligne. Vous êtes en train de changer de logiciel de comptabilité. Vous pouvez transférer les informations de l'ancien logiciel vers le nouveau en utilisant des fichiers CSV. Mais il y a un problème avec le fichier `products.csv`. En effet, la valeur de la colonne `archived` est notée `VRAI` ou `FAUX`. Mais le nouveau logiciel ne supporte que `TRUE` ou `FALSE`.
Donc ouvrez le fichier avec Python, modifiez la valeur de la colonne `archived` en `TRUE` ou `FALSE` et écrivez le nouveau fichier dans le dossier `parsed_data`.

## Exercice 5 - Ajouter la monnaie en fonction du pays

Toujours pour votre nouveau logiciel de comptabilité, il vous demande obligatoirement une devise (EUR, USD, GBP, etc.) pour chaque utilisateur.

Actuellement, dans le fichier `users.csv`, vous avez le pays de l'utilisateur. Utilisez-le pour ajouter une colonne `currency`, avec les valeurs suivantes :
- FR, ES : EUR
- US : USD
- UK : GBP

## Exercice 6 - Calculer la somme des achats par utilisateur

Votre collègue commercial souhaite faire une campagne pour remercier vos meilleurs clients. Pour cela, il vous demande la somme totale des achats de chaque utilisateur, et de lui fournir les emails et noms des 3 meilleurs clients.

Créez un script Python qui, à l'aide des fichiers `users.csv`, `invoices.csv` et `orders.csv`, affichera dans la console les emails et noms des 3 meilleurs clients, avec la somme totale de leurs achats.

<details>
<summary>Aide</summary>

Pour calculer la somme des achats de chaque utilisateur, lisez le fichier `orders.csv` et récupérez le prix de chaque `invoice_id`. Puis regroupez chaque `invoice_id` par `user_id`, faites la somme globale et trouvez les 3 plus élevés (pour trouver les 3 plus élevés, il faut trier les valeurs et prendre les 3 dernières en cas d'ordre croissant). Regardez du côté de la fonction `sorted` (https://docs.python.org/3/howto/sorting.html).

</details>

## Exercice 7 - Créer son propre logiciel de comptabilité (Programmation Orientée Objet)

Finalement, personne n'aime votre nouveau logiciel de comptabilité. Vous avez donc décidé d'en créer un.

Nous allons créer une version simplifiée d'un magasin en ligne de commande. Celui-ci sera capable de lire les fichiers CSV, de les modifier et de les sauvegarder à nouveau dans des fichiers CSV.

> Le code produit sera une approche très basique et simplifiée, mais il permettra de mettre en pratique la programmation orientée objet.

Nous allons créer 4 classes, une pour chaque fichier CSV :
- `User`
- `Product`
- `Order`
- `Invoice`

Chacune de ces classes instanciera les en-têtes des fichiers CSV en tant qu'attributs (exemple : un utilisateur possédera les attributs `id`, `lastname`, `firstname`, `email`, etc.). Dans le cas des `Orders`, au lieu de stocker un identifiant d'un autre objet, nous stockerons directement son instance. Exemple : au lieu de stocker un `user_id`, nous stockerons directement un objet `User`.

Chaque classe possédera 3 méthodes statiques pour interagir avec les fichiers CSV :
- `get` : qui récupérera directement l'instance de la classe en fonction de son id et la retournera.
- `load` : qui lira le fichier CSV et retournera une liste d'instances de la classe.
- `save` : qui écrira les instances dans le fichier CSV.

> Pour que cela fonctionne, vous devrez avoir un attribut statique `instances` qui stockera toutes les instances de la classe.

<details>
<summary>Conseils</summary>
La méthode `load` de `Order` devra utiliser les méthodes `get` de `Invoice` et `User`.
</details>

Le programme démarre en déclenchant la méthode `load` de toutes les classes.

Quelques fonctionnalités:
- Les `Product` possède une methode `remove_from_stock` qui permet de retirer une quantité de produit du stock
- Les `Order` possède une methode `get_total_price` qui permet de récupérer le prix total d'une commande (prix unitaire * quantité)


Ensuite, créez un menu en console qui permettra de :
- créer un utilisateur
- créer un produit
- créer une commande (qui permet de renseigner plusieurs produits et quantités)
- sauvegarder les données

> Pour centraliser la logique d'interaction avec les fichiers CSV, il est conseillé de créer une classe mère abstraite `CsvModel` qui contiendra la logique commune du traitement des fichiers CSV.

> Pour parser les dates, il est conseillé d'utiliser la bibliothèque `datetime` (https://docs.python.org/3/library/datetime.html), notamment la fonction `strptime`.

> Essayez de faire en sorte que le programme ne crash pas en cas d'erreur de saisie utilisateur.

### Pour aller plus loin
- Ajoutez une commande qui permet de récupérer les N plus gros acheteurs (vous aurez peut-être besoin de créer plus d'associations entre les classes)
- Ajoutez des filtres sur la création d'instance (exemple : le mail doit être valide, le prix doit être positif, etc.)
- Ajouteé des commandes supplémentaires (exemple: afficher tous les produits, afficher tous les utilisateurs, etc...)