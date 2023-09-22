def insere(lista_numero, n):
    """Função que, dada uma lista ordenada (crescente) de números inteiros
e um número inteiro n, inclue n na posição correta, de tal maneira que
a lista continue ordenada.
list , int -> list"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero