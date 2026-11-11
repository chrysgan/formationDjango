personnage = {'nom': 'Tintin', 'metier': 'Reporter', 'age': 17}
personnage['compagnon'] = 'Milou'
personnage['age'] = 18
print(len(personnage))
print(personnage.get('nationalite', 'belge'))
for cle,valeur in personnage.items():
    print(f"{cle} : {valeur}")
