def intercala(lista1, lista2): #AULA 5
    """Retorne uma lista3 intercalando elementos de outras duas listas;
    list, list -> list"""
    lista3 = []
    i = 0
    lista3 += [lista1[i],lista2[i]]
    i = 1
    lista3+= [lista1[i],lista2[i]]
    i = 2
    lista3 += [lista1[i],lista2[i]]
    return lista3