def insere(lista_numero,n):
    """ Função que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclue n na posição correta, ou seja, de tal maneira que a lista continue ordenada;
        list -> list;"""
    lista_ordenada = lista_numero + [n]
    lista_ordenada = list.sort(lista_ordenada)
    return lista_ordenada