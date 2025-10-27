
import os
import input
import file

data = [{"titre": "Inception","année": 2010,"genre": "SF","vu": True}, 
        {"titre": "Titanic","année": 1997,"genre": "Romance","vu": False}]

def main():
    if not os.path.exists("anime_database.csv"):
        file.file_creation()
    else:
        if input.file_overwrite():
            file.file_creation()

    
    





def ajouter_anime():
    pass



if __name__ == '__main__':
    main()
