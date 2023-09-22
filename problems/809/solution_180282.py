#1

def terceiralista(L1,L2):

    '''Função que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2'''

    # list, list -> list

    L3 = list()

    L3.append(L1[0]), L3.append(L2[0]), L3.append(L1[1]), L3.append(L2[1]), L3.append(L1[2]), L3.append(L2[2])

    return L3