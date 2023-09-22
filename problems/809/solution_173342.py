def intercala (lista1, lista2):
    """Função que, tendo como entrada duas listas de 3 elementos cada, gera uma lista 3 com os elementos de L1 e L2 intercalados
    entrada: list, list
    saída: list"""
    
    lista3[1] = lista1[1]
    lista3[2] = lista2[1]
    lista3[3] = lista1[2]
    lista3[4] = lista2[2]
    lista3[5] = lista1[3]
    lista3[6] = lista2[3]
    
    return list(lista3)