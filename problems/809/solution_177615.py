def intercala(lista1, lista2):
    """Função que recebe duas listas e retorna a concatenção de seus elementos de forma intercalada"""
    lista3 = []
    lista1[0] = lista3[0]
    lista2[0] = lista3[1]
    lista1[1] = lista3[2]
    lista2[1] = lista3[3]
    lista1[2] = lista3[4]
    lista2[2] = lista3[5]
    return lista3