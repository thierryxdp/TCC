def insere(lista_numero,n):
    """
    Dada uma lista ordenada (crescente) de numeros inteiros e um numero
    inteiro n, inclua n na posição correta;
    list, int -> list
    """
    if n-1 in lista_numero:
        lista = list.index(lista_numero,n-1)
        nova = lista_numero[:lista] + [n] + lista_numero[lista:]
        return nova
    if n-2 in lista_numero:
        lista = list.index(lista_numero,n-2)
        nova = lista_numero[:lista] + [n] + lista_numero[lista:]
        return nova
    if n-3 in lista_numero:
        lista = list.index(lista_numero,n-3)
        nova = lista_numero[:lista] + [n] + lista_numero[lista:]
        return nova
    if n-4 in lista_numero:
        lista = list.index(lista_numero,n-4)
        nova = lista_numero[:lista] + [n] + lista_numero[lista:]
        return nova
    else:
        return "Problema"