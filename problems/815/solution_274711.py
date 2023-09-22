def insere(lista_numero, n):
    '''
    	Funcao que dada uma lista ordenada (crescente) de numeros
        inteiros e um numero inteiro, retorna a lista inclindo n na
        posição correta
    '''
    L = lista_numero
    list.append(L, n)
    list.sort(L)
    return L