def insere(lista,n):
    """dada uma lista ordenada de numeros inteiros e um numero inteiro n, inclui n na posicao correta, ou seja, de maneira que a lista continue ordenada
    list, int -> list"""
    list.insert(lista,0,n)
    list.sort(lista)
    return lista