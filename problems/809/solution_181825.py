def intercala(L1, L2):
    """funcao que, dada duas listas de tamanho 3, intercala os elementos de L1 e L2
list,list -> list"""
    L3 = [L1[0],] + [L2[0],] + [L1[1],] + [L2[1],] + [L1[2],] + [L2[2]]
    return L3