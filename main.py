
import os
import input
import file

data = [{"titre": "Chihayafuru","année": 2010,"genre": "Romance","vu": 1}, 
        {"titre": "Kingdom","année": 2008,"genre": "Shonen","vu": 0}]

def main():
    if not os.path.exists("anime_database.csv"):
        file.file_creation(data)
    """else:
        if input.file_overwrite():
            file.file_creation(data)"""

    banniere = input.title()

    while True:
        # Affiche le menu principal et la banniere
        print(banniere)
        menu = input.main_menu()

        # Appelle la fonction selectionnée dans le menu
        print(banniere)
        match menu:
            case "1":
                break
            case "2":
                animeList = read_anime_list()
                for row in animeList:
                    print(anime_to_string(row))
            case "3":
                title = input.find_anime()
                if title is None:
                    print("Titre invalide")
                else:
                    anime = rechercher_anime(title)
                    if anime is None:
                        print("Impossible de trouver cet anime")
                    else:
                        print(anime_to_string(anime))
            case "4":
                if not ajouter_anime():
                    print("Anime déjà present")
            case "5":
                pass
            case "6":
                anime = input.delete_anime()
                file.file_creation(supprimer_anime(anime))
            case _ :
                print("Commande non reconnue")
        print(input.stop_display())

def ajouter_anime():
    anime = input.add_anime_input()
    # fonction pour verifier que l'anime n'ets pas encore dans la liste
    if not rechercher_anime(anime):
        file.add_anime(anime)
        return True
    return False


def read_anime_list():
    data = file.file_read()
    return data

def anime_to_string(row):
    vu = ", vu" if int(row['vu']) else ""
    return f"{row['titre']}: anime de type {row['genre']} sorti en {row['année']}{vu}."

def rechercher_anime(anime):
    animeList = read_anime_list()
    for row in animeList:
        if row["titre"].lower() == anime["titre"].lower():
            return row
    return None
    
def supprimer_anime(titre):
    newData = []
    for anime in file.file_read():
        if anime["titre"] != titre:
            newData.append(anime)
    return newData


if __name__ == '__main__':
    main()
