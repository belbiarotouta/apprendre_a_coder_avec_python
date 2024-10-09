numerateur = 2
denominateur = 10
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numérateur ou dénominateur n'a pas été définie.")
except TypeError:
    print("La variable numérateur ou dénominateur est d'un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable dénominateur est égale à 0.")
else:
    print(f"Le résultat obtenu est: {resultat}")