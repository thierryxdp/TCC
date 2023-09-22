def maiores(lista_numero, n):
    """ dada uma lista ordenada de numeros crescentes 
        inteiros e um numero inteiro n, inclua n na posicao
        correta de uma maneira que a lista continue ordenada
        : list, int --> list 
    """
    lista_numero = [13,17,9,19]
    list.append(lista_numero, n)
    list.sort(lista_numero)
    list.index(lista_numero,n)
    return lista_numero [2:5]