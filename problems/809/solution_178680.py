def intercala(L1,L2):
    '''Função que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3'''
    list.insert(L1,1,L2[0])
    list.insert(L1,3,L2[1])
    list.insert(L1,5,L2[2])
    return L1