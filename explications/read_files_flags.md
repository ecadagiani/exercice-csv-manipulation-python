# Les modes d'ouverture de fichiers en Python 📂

Imaginons que les fichiers sont comme des livres dans une bibliothèque. Selon ce que vous voulez faire, vous avez différentes permissions !

## Les modes de base 📚

### Mode 'r' (read) - Le lecteur 👀
````python
with open('fichier.txt', 'r') as f:
    contenu = f.read()
````
- Mode par défaut
- Lecture seule
- ⚠️ Erreur si le fichier n'existe pas
- Comme emprunter un livre : vous pouvez lire mais pas écrire dedans !

### Mode 'w' (write) - L'auteur ✍️
````python
with open('fichier.txt', 'w') as f:
    f.write('Nouveau contenu')
````
- Écriture seule
- Crée le fichier s'il n'existe pas
- ⚠️ **ATTENTION** : Efface tout le contenu existant !
- Comme prendre une nouvelle page blanche : l'ancien contenu disparaît

### Mode 'a' (append) - L'annotateur 📝
````python
with open('fichier.txt', 'a') as f:
    f.write('Ajout à la fin')
````
- Ajout à la fin du fichier
- Crée le fichier s'il n'existe pas
- Ne supprime pas le contenu existant
- Comme ajouter des post-it à la fin d'un livre

## Les modes avancés 🔄

### Mode 'r+' - Le réviseur 📖
````python
with open('fichier.txt', 'r+') as f:
    contenu = f.read()
    f.write('Modification')
````
- Lecture ET écriture
- ⚠️ Le fichier doit exister
- Le curseur commence au début
- Comme avoir un crayon tout en lisant le livre

### Mode 'w+' - L'effaceur créatif ✨
````python
with open('fichier.txt', 'w+') as f:
    f.write('Nouveau contenu')
    f.seek(0)  # Retour au début
    contenu = f.read()
````
- Lecture ET écriture
- ⚠️ Efface tout le contenu existant
- Crée le fichier s'il n'existe pas
- Comme prendre une nouvelle page pour écrire et relire

### Mode 'a+' - L'archiviste 📚
````python
with open('fichier.txt', 'a+') as f:
    f.write('Ajout')
    f.seek(0)  # Retour au début pour lire
    contenu = f.read()
````
- Lecture ET ajout
- Crée le fichier s'il n'existe pas
- Le curseur commence à la fin
- Comme ajouter des notes tout en pouvant relire le livre

## Bonus : Les modes binaires 🤖

Ajoutez 'b' à n'importe quel mode pour traiter le fichier en binaire :
- 'rb' : lecture binaire
- 'wb' : écriture binaire
- etc.

````python
# Pour les images par exemple
with open('image.jpg', 'rb') as f:
    data = f.read()
````

## Tableau récapitulatif 📊

| Mode | Lecture | Écriture | Crée le fichier | Efface le contenu | Position curseur |
|------|---------|----------|-----------------|-------------------|------------------|
| 'r'  | ✅      | ❌       | ❌              | ❌                | Début           |
| 'w'  | ❌      | ✅       | ✅              | ✅                | Début           |
| 'a'  | ❌      | ✅       | ✅              | ❌                | Fin             |
| 'r+' | ✅      | ✅       | ❌              | ❌                | Début           |
| 'w+' | ✅      | ✅       | ✅              | ✅                | Début           |
| 'a+' | ✅      | ✅       | ✅              | ❌                | Fin             |

## Conseil pratique 💡

Toujours utiliser le context manager (`with`) pour gérer proprement la fermeture des fichiers :
````python
# Bonne pratique ✅
with open('fichier.txt', 'r') as f:
    contenu = f.read()

# À éviter ❌
f = open('fichier.txt', 'r')
contenu = f.read()
f.close()  # Il faut penser à fermer le fichier
````
