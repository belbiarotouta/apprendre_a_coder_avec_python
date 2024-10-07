year = input("Entrer une annnée: ")

try:
    year = int(year)
    if year == 0:
        raise ValueError
except ValueError:
    print("La valeur saisie est invalide(l'année est peut-être nulle)")
