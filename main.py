
import os
import input
import file

data = [{"titre": "Inception","année": 2010,"genre": "SF","vu": True}, 
        {"titre": "Titanic","année": 1997,"genre": "Romance","vu": False}]

def main():
    if not os.path.exists("anime_database.csv"):
        file.file_creation(data)
    else:
        if input.file_overwrite():
            file.file_creation(data)

    while True:
        ajouter_anime()
    
    





def ajouter_anime():
    anime = input.add_anime_input()

    # fonction pour verifier que l'anime n'ets pas encore dans la liste

    file.add_anime(anime)



if __name__ == '__main__':
    main()
