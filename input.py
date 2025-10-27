

def file_overwrite():
    while True:
        overwrite = input("""
Un fichier portant ce nom existe deja.
Que voulez-vous faire?
1 - Effacer le fichier et repartir de zero
2 - Continuer à partir du même fichier
Votre choix: """).strip()
        if overwrite in "12" and len(overwrite) == 1:
            return True if overwrite == "1" else False
        print("Commande non reconnue, veuillez entrer 1 ou 2")


def add_anime_input():
    while True:
        print(("""
Ajouter un nouvel anime à la liste
"""))
        while True:
            name = input ("""
Entrez le nom de l'anime
Titre: """).strip()
            if len(name) > 0:
                break

        while True:
            genre = input("""
Entrez le genre de l'anime
Genre: """).strip()
            if len(genre) > 0:
                break

        while True:
            date = input("""
Entrez la date de l'anime en format XXXX
Année: """).strip()
            if date.isdigit() and len(date) == 4:
                date = int(date)
                break

        return {"titre": name, "année": date, "genre": genre, "vu": False}