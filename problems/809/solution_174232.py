def intercala_listas(lista1,lista2):
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista