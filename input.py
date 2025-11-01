import os

def title():
    os.system("cls" if os.name == "nt" else "clear")
    return """
-----------------------
|    Anime Manager    |
-----------------------"""


def menu_options():
    return """
Que souhaitez-vous faire?
[bold cyan]1[/bold cyan] - Quitter le programme
[bold cyan]2[/bold cyan] - Consultez la liste des animes
[bold cyan]3[/bold cyan] - Chercher un anime dans la liste
[bold cyan]4[/bold cyan] - Ajouter un anime à la liste
[bold cyan]5[/bold cyan] - Modifier le statut d'un anime
[bold cyan]6[/bold cyan] - Supprimer un anime de la liste
[bold cyan]7[/bold cyan] - Exporter la liste au format Json
[bold cyan]8[/bold cyan] - Statistiques"""

def main_menu():
    while True:
        menu = input("Votre choix: ").strip()
        if menu in "12345678" and len(menu) == 1:
            return menu
        return None


def stop_display():
    return input("Appuyer sur la touche Entrée pour continuer.")

'''def file_overwrite():
    while True:
        overwrite = input("""
Un fichier portant ce nom existe deja.
Que voulez-vous faire?
[bold cyan]1[/bold cyan] - Effacer le fichier et repartir de zero
[bold cyan]2[/bold cyan] - Continuer à partir du même fichier
Votre choix: """).strip()
        if overwrite in "12" and len(overwrite) == 1:
            return True if overwrite == "1" else False
        print("Commande non reconnue, veuillez entrer 1 ou 2")'''


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
           