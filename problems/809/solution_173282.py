def intercala (lista1,lista2):
    '''
    A função retorna uma lista intercalada
    entre as duas.
    Lista,Lista -> Lista
    '''
    lista = []

    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])

    return lista