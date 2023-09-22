def intercala(L1,L2):
    '''
    funcao que dadas duas listas L1 e L2 de
    tamanho 3, retorna uma lista L3 formada
    pelos elementos de L1 e L2 intercalados
    list, list -> list
    '''
    L3=L1+L2
    L1=L3[::2]
    L2=L3[1::2]
    return L3