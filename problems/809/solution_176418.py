def intercala(lista1, lista2):
    """função que alternar os elementos da lista 1 com a lista 2 resultando na lista 3"""
    """list, list -> list"""
    lista3 = []
    i=3
    for i in range(0,len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        lista3.append(lista1[i+1])
        lista3.append(lista2[i+1])
        lista3.append(lista1[i+2])
        lista3.append(lista2[i+2])
        return lista3