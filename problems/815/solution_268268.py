def insere(lista_numero,n):
    """Função que, dada uma lista ordenada (crescente) de números inteiros e um número, inclui n na posição correta, ou seja, de tal maneira que a lista continue ordenada
       list, int -> list"""
    lista_numero.sort(lista_numero,n)
    return lista_numero