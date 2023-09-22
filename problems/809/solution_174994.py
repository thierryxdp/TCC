def intercala(lista1, lista2):
    """Dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 intercalando os elementos de L1 e L2
    lista, lista -> lista"""
    L3=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]
    return L3