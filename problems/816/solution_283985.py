def maiores(lista_numero, n):
    """ dada uma lista ordenada de numeros crescentes 
        inteiros e um numero inteiro n, inclua n na posicao
        correta de uma maneira que a lista continue ordenada
        : list, int --> list 
    """
    list.append(lista_numero, n)
    list.sort(lista_numero)
    list.index(lista_numero,n)
    list.max(lista_numero,n)
    return lista_numero