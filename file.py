import csv

def file_creation(data: list[dict]):
    with open("anime_database.csv", "w", encoding="utf-8", newline="") as file:
        champs = ["titre", "année", "genre", "vu"]
        writer = csv.DictWriter(file, fieldnames=champs)
        writer.writeheader()
        writer.writerows(data)

def file_read():
    with open("anime_database.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        return rows


def add_anime(anime: dict):
    with open("anime_database.csv", "a", encoding="utf-8", newline="") as file:
        champs = ["titre", "année", "genre", "vu"]
        writer = csv.DictWriter(file, fieldnames=champs)
        writer.writerow(anime)
