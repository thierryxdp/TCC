def insere(listaNums,n):
    ''' essa funcao retorna uma lista ordenada, e acrescenta-se o
    numero 'n' a ela, retornando de forma ordenada'''
    listaFinal = listaNums + [n]
    listaFinal.sort()
    return listaFinal