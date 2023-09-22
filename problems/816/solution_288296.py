def maiores(lista,n):
    """Função que dada uma lista e um número "n", retorna uma lista que tem todos os números da primeira maiores que "n", em ordem crescente. list -> list"""
    l = []
    for i in range(len(lista)):
        if lista[i] > n:
            l.append(lista[i])
    l.sort()
    return l