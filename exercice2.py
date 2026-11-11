albums = [
    {"titre": "Tintin au pays des Soviets", "annee": 1930, "couleur": False},
    {"titre": "Le Lotus bleu", "annee": 1936, "couleur": False},
    {"titre": "Objectif Lune", "annee": 1953, "couleur": True},
    {"titre": "Tintin et les Picaros", "annee": 1976, "couleur": True},
]
for alb in albums:
    print(f"{alb['annee']} - {alb['titre']}")

en_couleur = [alb["titre"] for alb in albums if alb["couleur"]]
print(en_couleur)

avant_1950 = [alb["annee"] for alb in albums if alb["annee"] < 1950]
print(avant_1950)

print(len(en_couleur))