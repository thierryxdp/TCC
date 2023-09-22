def intercala(lista1, lista2):
 'intercala 2 listas, retorando uma terceira. list, list -> list'
    lista3 = []
    L3 = lista3
    L1 = lista1
    L2 = lista2
    return L3+(L1[:1])+(L2[:1])+(L1[1:2])+(L2[1:2])+(L1[2:3])+(L2[2:3])+(L1[3:4])+(L2[3:4])+(L1[4:5])+(L2[4:5])+(L1[5:6])+(L2[5:6])+(L1[6:7])+(L2[6:7])+(L1[7:8])+(L2[7:8])