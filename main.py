
import os
import input
import file

data = [{"titre": "Chihayafuru","année": 2010,"genre": "Romance","vu": "True"}, 
        {"titre": "Kingdom","année": 2008,"genre": "Shonen","vu": "False"}]

def main():
    if not os.path.exists("anime_database.csv"):
        file.file_creation(data)

    banniere = input.title()

    while True:
        # Affiche le menu principal et la banniere
        print(banniere)
        menu = menu_principal()
        if menu is None:
            break
        
        # Appelle la fonction selectionnée dans le menu
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
            title = input.find_anime()
            if title is None:
                return "Titre invalide"
            else:
                anime = rechercher_anime(title)
                if anime is None:
                    return "Impossible de trouver cet anime"
                else:
                    return anime_to_string(anime)
        case "4":
            return ajouter_anime()   
        case "5":
            titre = input.modify_status()
            data, modification = voir(titre)
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
        case _ :
            return "Commande non reconnue"



def ajouter_anime():
    anime = input.add_anime_input()
    print(anime)
    # fonction pour verifier que l'anime n'ets pas encore dans la liste
    if rechercher_anime(anime["titre"]) is not None:
        return "Anime déjà présent dans la liste"
    file.add_anime(anime)
    return "Anime correctement ajouté à la liste"
    


def read_anime_list():
    data = file.file_read()
    return data

def anime_to_string(row):
    vu = ", vu" if row['vu'] == "True" else ""
    return f"{row['titre']}: anime de type {row['genre']} sorti en {row['année']}{vu}."

def rechercher_anime(titre:str):
    animeList = read_anime_list()
    for row in animeList:
        if row["titre"].lower() == titre.lower():
            return row
    return None
    
def supprimer_anime(titre):
    newData = []
    suppression = "Aucun anime de ce nom n'as été trouvé"
    for anime in file.file_read():
        if anime["titre"] == titre:
            suppression = "L'anime a bien été supprimé"
        else:
            newData.append(anime)
    return newData, suppression

def voir(titre):
    newData = []
    modification = "Aucun Anime de ce nom n'as pu être trouvé"
    for anime in file.file_read():
        if anime["titre"] == titre:
            if anime["vu"] == "True":
                modification = "Cet Anime était déjà marqué comme vu"
            else:
                modification = "Cet Anime est désormais marqué comme vu"
            anime["vu"] = "True"
            newData.append(anime)
        else:
            newData.append(anime)
    return newData, modification


if __name__ == '__main__':
    main()
