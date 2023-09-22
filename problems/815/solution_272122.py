def insere (lista_numero, n):
    '''dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro, retorna uma lista com o numero inteiro na
       posiçao correta.
       : list, int -> list
    '''
    lis_aux = lista_numero.append(n)
    return lis_aux