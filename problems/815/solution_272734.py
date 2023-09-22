def insere(lista_numero,n):
    """
    Dada uma lista ordenada (crescente) de numeros inteiros e um numero
    inteiro n, inclua n na posição correta;
    list, int -> list
    """
    if n-1 in lista_numero:
        lista = list.index(lista_numero,n-1)
        nova = lista_numero[:lista+1] + [n] + lista_numero[lista+1:]
        return nova
    else:
        return "Problema"