def maiores(lista_numero, n):
    '''
    	Funcao que dada uma lista ordenada (crescente) de numeros
        inteiros e um numero inteiro, retorna a lista somente com 
        os numeros maiores que n.
    '''
    L = lista_numero
    list.append(L, n)
    list.sort(L)
    del L[0:list.index(L, n)]
    return L