import os

def title():
    os.system("cls" if os.name == "nt" else "clear")
    return """
-----------------------
|    Anime Manager    |
-----------------------"""


def main_menu():
    while True:
        menu = input("""
Que souhaitez-vous faire?
1 - Quitter le programme
2 - Consultez la liste des anime
3 - Chercher un anime dans la liste
4 - Ajouter un anime à la liste
5 - Modifier le statut d'un anime
6 - Supprimer un anime de la liste
Votre choix: """).strip()
        if menu in "123456" and len(menu) == 1:
            return menu
        return None


def stop_display():
    return input("Appuyer sur la touche Entrée pour continuer.")

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

        return {"titre": name, "année": date, "genre": genre, "vu": "False"}
    

def find_anime():
    while True:
        anime = input("""
Veuillez entrer le nom de l'anime que vous voulez consulter
Titre: """).strip()
        if len(anime) > 0:
            return anime
        return None
    

def delete_anime():
    while True:
        anime = input("""
Veuillez entrer le nom de l'anime que vous voulez supprimer
Titre: """).strip()
        if len(anime) > 0:
            return anime
        return None
    

def modify_status():
    while True:
        anime = input("""
Veuillez entrer le nom de l'anime que vous avez vu
Titre: """).strip()
        if len(anime) > 0:
            return anime
        return None
    
if __name__ == '__main__':
    main_menu()
           