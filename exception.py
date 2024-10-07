year = input("Entrer une année: ")

try: # On essaye de convertir l'année en entier.
    year = int(year)
    print(f"Voici l'année: {year}")
except:
    print("Erreur lors de la conversion de l'année.")