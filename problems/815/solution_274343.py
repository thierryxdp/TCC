def insere(lista_numero, n):
    '''
    	Recebe uma lista ordenada e um número, e retorna a lista com o número digitado na posição correta de modo que a lista permaneça ordenada.
        Parâmetro 1: list
        Parâmetro 2: int
        Resultado: list
    '''
    lista_numero.append (n)
    lista_numero.sort()
    return lista_numero