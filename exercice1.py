year = int(input("Enter a year: "))

if year % 400 == 0:
    print("C'est une année bissextile", year)
elif year % 100 == 0:
    print("Ce n'est pas une année bissextile", year)
elif year % 4 ==0:
    print("C'est une année bissextile", year)
else:
    print("Ce n'est pas une année bissextile", year)

