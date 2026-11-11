albums = [
    {"titre": "Tintin au pays des Soviets", "annee": 1930, "couleur": False},
    {"titre": "Le Lotus bleu", "annee": 1936, "couleur": False},
    {"titre": "Objectif Lune", "annee": 1953, "couleur": True},
    {"titre": "Tintin et les Picaros", "annee": 1976, "couleur": True},
]


def decrire(album):
    couleur = "noir et blanc"
    if album["couleur"]:
        couleur = "couleur"
    return f"{album['titre']} ({album['annee']}), {couleur}"


def filtrer(albums, couleur=True):
    return [album for album in albums if album["couleur"] == couleur]


for album in filtrer(albums):
    print(decrire(album))

print(len(filtrer(albums, couleur=False)))
print(decrire(albums[0]) == decrire(albums[1]))
