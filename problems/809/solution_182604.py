def intercala(l1, l2):
    '''Dadas duas listas L1 e L2 de tamanho 3, gera 
    uma lista L3 formada intercalando os elementos de 
    L1 e L2'''
    l3= [l1[0]]+[l2[0]]+[l1[1]]+[l2[1]]+[l1[2]]+[l2[2]]
    return l3