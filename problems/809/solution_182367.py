def intercala(lista1, lista2):
    """dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2"""
    L1 = lista1
    L2 = lista2    
    L3 = [L1[0], L2[0], L1[1], L2[1], L1[2], L2[2]]
    return L3