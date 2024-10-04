def table_multiplication(nombre: int, maximum: int = 10) -> int:
    """Fonction affichant la table de multiplication par nombre.

    Arguments :
        nombre (int) : le nombre dont la table de multiplication est à afficher.
        maximum (int, optionnel) : afficher la table de 1 à maximum.

    """
    for i in range(1, maximum + 1):
        print(f"{i} * {nombre} : {i * nombre}")