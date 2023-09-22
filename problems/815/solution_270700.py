def insere(lista_numero,n):
    """função que recebe uma lista ordenada (crescente) de n ́umeros in-
    teiros e um número inteiro n, inclua n na posição correta, ou seja,
    de tal maneira que a lista continue ordenada.
    list,int -> list"""
    lista = list(lista_numero)
    lista.append(n)
    list.sort(lista)
    return list