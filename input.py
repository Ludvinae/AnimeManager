

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

