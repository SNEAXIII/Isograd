lines = ['4 1 1', '2', '4 1 0 3', '1 0 0 1']


def split(elem):
    splited = elem.split(" ")
    return int(splited[0]), int(splited[1]), int(splited[2]), int(splited[3])


recettes = tuple(map(split, lines[2:]))

print(recettes)


# mini_baie = min(lines[0].split(" "))
#
# print(mini_baie)
#
#

def boucle_recursif(nombre_iteration, nombre_boucle_restante=2,liste_temp=None ,liste=None ):
    if liste is None:
        liste = []

    if not nombre_boucle_restante == 0:
        liste_temp = []
        for a in range(nombre_iteration):
            liste_temp.append(a + 1)
            boucle_recursif(5, nombre_boucle_restante - 1, liste,liste_temp)
    else:
        liste.append(liste_temp)

    return liste


print(boucle_recursif(5, 2))
# liste = []
# for y in range(2):
#     liste_temp=[]
#     for x in range(2):
#
