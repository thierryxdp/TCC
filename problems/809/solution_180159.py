def intercala(lista1, lista2):
    '''Função que dadas as lista1 e lista2 retorne uma lista3 que é formada intercalando os elementos da lista1 e lista2; list, list -> list'''
    return (lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]