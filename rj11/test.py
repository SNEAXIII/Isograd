# lines = ['10 20', '1422 2198', '2112 2133', '534 2323', '2119 2165', '2420 2456', '1664 2304', '718 1726', '1674 2024', '1740 2398', '1498 1516', '1963 2303', '2322 2343', '1146 1466', '2106 2132', '622 2422', '176 784', '174 830', '1288 2147', '2072 2196', '1657 2109']

lines = ['10 21', '973 991', '1391 1568', '111 2073', '1030 1312', '125 465', '1527 1559', '1654 2162', '1099 2029',
         '2086 2395', '2404 2438', '2414 2431', '613 1469', '742 1647', '1245 2196', '259 1991', '379 1351', '285 493',
         '1143 2215', '1669 2259', '1832 2432', '2039 2233']

# lines = ['10 30', '650 2400', '2367 2469', '2236 2387', '1317 2323', '849 1793', '264 866', '1552 2216', '1163 1611', '2043 2199', '2493 2494', '932 1614', '1546 2349', '256 494', '1059 1261', '1757 2099', '1537 1744', '297 1895', '2420 2448', '2158 2470', '639 1464', '1983 2257', '674 1928', '201 313', '1971 2282', '666 1558', '763 1965', '283 2420', '686 1837', '123 1530', '1577 2308']

# lines = ['10 23', '962 1397', '2328 2471', '163 795', '864 1756', '25 685', '721 1011', '507 2132', '2037 2152', '165 311', '363 1968', '1596 1865', '1845 2453', '1452 2088', '824 2105', '1974 2321', '1552 1916', '931 2465', '366 580', '1530 1844', '1085 1780', '1337 2133', '251 1156', '907 1569']

table_requetes = [[int(elem.split()[0]), int(elem.split()[1])] for elem in lines[1:]]
print(table_requetes)
table_des_cable = [[] for _ in range(int(lines[0].split(" ")[0]))]
print(table_des_cable)
rendu_final = ""

for requete in table_requetes:
    debut,fin = requete[0],requete[1]
    valide = True
    for index in range(len(table_des_cable)):
        table_des_cable[i]

# liste_exemple = [f"{a} {a + 1}" for a in range(0, 20)]
# liste_exemple[0] = ""

# class liste_parsee:
#
#     def __init__(self, liste_base):
#         self.longueur = None
#         self.liste_parsee = None
#         self.genere_liste_parsee(liste_base)
#
#     def __str__(self):
#         return f"{self.est_possible()}"
#
#     def genere_liste_parsee(self, liste):
#         liste_formatee = []
#         self.nombre_cable = int(liste[0].split(" ")[0])
#         mini, maxi = int(liste[1].split(" ")[0]), int(liste[1].split(" ")[1])
#         for i, elem in enumerate(liste[1:]):
#             elem_split = elem.split(" ")
#             elem_split_int = [int(elem_split[0]), int(elem_split[1]), i, None]
#             liste_formatee.append(elem_split_int)
#             mini, maxi = min(mini, elem_split_int[0]), max(maxi, elem_split_int[1])
#         for y in range(len(liste_formatee)):
#             for x in range(2):
#                 liste_formatee[y][x] -= mini
#         self.liste_parsee = sorted(liste_formatee, key=lambda x: x[0])
#         self.longueur = maxi - mini
#
#     def est_possible(self):
#         table_des_cables = [0 for _ in range(self.nombre_cable)]
#         occurrence = [0 for _ in range(self.longueur)]
#         for i, elem in enumerate(self.liste_parsee):
#             valide = False
#             for cable in range(len(table_des_cables)):
#                 if elem[0] >= table_des_cables[cable]:
#                     table_des_cables[cable] = elem[1]
#                     self.liste_parsee[i][3] = cable
#                     valide = True
#                     break
#             if not valide: return "Pas possible"
#         self.liste_parsee = sorted(self.liste_parsee, key=lambda x: x[2])
#         cables_ordones = ""
#         for elem in self.liste_parsee:
#             cables_ordones += f"{elem[3]} "
#             # for index in range(elem[0], elem[1]):
#             #     occurrence[index] += 1
#             #     if occurrence[index] == self.nombre_cable:
#             #         return "Pas possible"
#         return cables_ordones[:-1]
#
# instance = liste_parsee(lines)
# print(instance)

# sys.stderr.write(f"lines = {lines}")
