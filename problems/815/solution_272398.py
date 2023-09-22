def insere(lista,n):
    """Dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta.
    list,int -> list"""
    lista=lista+[n]
    list.sort(lista)
    return lista