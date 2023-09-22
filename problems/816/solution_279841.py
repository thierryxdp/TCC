def maiores(lista, n):
    """Função que dada uma lista de números inteiros(lista) e um número
    inteiro(n), retorna outra lista que contenha todos os números da lista
    original maiores n.
    lista, int -> lista"""

    lista[0:0] = [n]
    list.sort(lista)
    a = lista[(list.index(lista,n))+1:]
    return a