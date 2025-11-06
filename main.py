import os
from rich import print
import Levenshtein
import input
import file

data = [{"titre": "Chihayafuru","année": 2011,"genre": "Romance","vu": True}, 
        {"titre": "Kingdom","année": 2012,"genre": "Shonen","vu": False},
        {"titre": "Sousou no Frieren","année": 2023,"genre": "Adventure","vu": True},
        {"titre": "Ace of diamond", "année": 2013, "genre": "Sport", "vu": True},
        {"titre": "Gintama","année": 2006,"genre": "Comedy","vu": True},
        {"titre": "Fullmetal alchemist","année": 2003,"genre": "Shonen","vu": True}]

def main():
    if not os.path.exists("anime_database.csv"):
        file.file_creation(data)

    banniere = input.title()

    while True:
        # Affiche le menu principal et la banniere
        print(banniere)
        print(input.menu_options())
        # Appelle la fonction selectionnée dans le menu
        menu = menu_principal()
        if menu is None:
            break
        
        # Affiche le résultat de l'option choisie dans le menu
        print(banniere)
        print(menu)
        print(input.stop_display())


def menu_principal():
    menu = input.main_menu()
    match menu:
        case "1":
            return None
        case "2":
            animeList = read_anime_list()
            string = ""
            for row in animeList:
                string += anime_to_string(row) + "\n"
            return string
        case "3":
            titre = input.find_anime()
            if titre is None:
                return "Titre invalide"
            else:
                anime = rechercher_anime(titre)
                if anime is None:
                    return f"Impossible de trouver {titre}"
                else:
                    return anime_to_string(anime)
        case "4":
            return ajouter_anime()   
        case "5":
            titre = input.modify_status()
            data, modification = marquer_comme_vu(titre)
            file.file_creation(data)
            return modification
        case "6":
            anime = input.delete_anime()
            data, suppression = supprimer_anime(anime)
            file.file_creation(data)
            return suppression
        case "7":
            file.export_list()
            return "Les données ont été exportées"
        case "8":
            stats = statistiques()
            return f"""
Statistiques:
Nombre d'animes dans la liste: {stats["longueur"]}
Animes vus / non vus: {stats["vu"]} / {stats["longueur"] - stats["vu"]}
Genre le plus representé: {max(stats["genres"])}
"""
        case _ :
            return "Commande non reconnue"



def ajouter_anime():
    anime = input.add_anime_input()
    # fonction pour verifier que l'anime n'ets pas encore dans la liste
    if rechercher_anime(anime["titre"]) is not None:
        return f"{anime["titre"]} déjà présent dans la liste"
    file.add_anime(anime)
    return f"{anime["titre"]} correctement ajouté à la liste"
    


def read_anime_list():
    data = file.file_read()
    return data

def anime_to_string(row):
    vu = ", vu" if row['vu'] == "True" else ""
    return f"{row['titre']}: anime de type {row['genre']} sorti en {row['année']}{vu}."

def rechercher_anime(titre:str):
    
    animeList = read_anime_list()
    for row in animeList:
        dst = Levenshtein.distance(row["titre"].lower(), titre.strip().lower())
        if dst < 3 or titre.strip().lower() in row["titre"].lower() :
            return row
    return None
    
def supprimer_anime(titre):
    newData = []
    suppression = "Aucun anime de ce nom n'as été trouvé"
    for anime in file.file_read():
        if anime["titre"] == titre:
            suppression = f"{titre} a bien été supprimé"
        else:
            newData.append(anime)
    return newData, suppression

def marquer_comme_vu(titre):
    newData = []
    modification = "Aucun Anime de ce nom n'as pu être trouvé"
    for anime in file.file_read():
        if anime["titre"] == titre:
            if anime["vu"] == "True":
                modification = f"{titre} était déjà marqué comme vu"
            else:
                modification = f"{titre} est désormais marqué comme vu"
            anime["vu"] = "True"
            newData.append(anime)
        else:
            newData.append(anime)
    return newData, modification

def statistiques():
    liste = file.file_read()
    longueur = len(liste)
    vu = 0
    genres = {}
    for anime in liste:
        if anime["vu"] == "True":
            vu += 1
        genre = anime["genre"]
        if genre not in genres:
            genres[genre] = 0
        genres[genre] += 1

    return {"longueur": longueur, "vu": vu, "genres": genres}


if __name__ == '__main__':
    main()
