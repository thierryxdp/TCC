def insere (lista_numero, n):
    '''dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro, retorna uma lista com o numero inteiro na
       posiçao correta.
       : list, int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero