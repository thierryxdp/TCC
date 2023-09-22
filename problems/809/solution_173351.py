def intercala (lista1, lista2):
    """Função que, tendo como entrada duas listas L1 e L2 de 3 elementos cada, gera uma lista 3 com os elementos de L1 e L2 intercalados
    entrada: list, list
    saída: list"""
    
    L3 = lista1 + lista2
    L3[::2] = lista1
    L3[1::2] = lista2
    return L3