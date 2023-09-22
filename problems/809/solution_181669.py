def intercala(lista1, lista2):
    lista3 = []
    for i in range(0,len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3

intercala([1,3,5],[2,4,6])