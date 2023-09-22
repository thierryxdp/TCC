def intercala(lista1, lista2):
    '''recebe duas listas de tamanho 3 e retorna uma terceira lista 
    com 6 elementos intercalados entre as duas listas dadas pelo usuario.'''
    L3 = list(zip(lista1, lista2))
    return [elt for sublist in L3 for elt in sublist]