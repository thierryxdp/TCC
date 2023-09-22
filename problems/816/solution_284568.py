def maiores(lista_numero,n):
    """funçao que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista 
    original maiores que n, ordenados em ordem crescente
    list->list"""
    list.append(lista_numero,n)
    list.sort(lista_numero,reverse=True)
    a=list.index(lista_numero,n)
    b=lista_numero[:a]
    list.sort(b)
    return b