liste_exemple = ['10 20', '1422 2198', '2112 2133', '534 2323', '2119 2165', '2420 2456', '1664 2304', '718 1726',
                 '1674 2024', '1740 2398', '1498 1516', '1963 2303', '2322 2343', '1146 1466', '2106 2132', '622 2422',
                 '176 784', '174 830', '1288 2147', '2072 2196', '1657 2109']

liste_formatee = []
liste_max = []
for elem in liste_exemple:
    elem_split = elem.split(" ")
    elem_split_int = int(elem_split[0]), int(elem_split[1])
    liste_formatee.append(elem_split_int)
    liste_max.append(elem_split_int[1])
    # print(elem_split[1])
print(max(liste_max))
print(liste_max)