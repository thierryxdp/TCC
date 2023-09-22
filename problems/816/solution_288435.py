def maiores(lista,n):
    """Dada uma lista de números inteiros e um número int,
    retorna outra lista, que contem todos s números da lista 
    original maiores que n, ordenados em ordem crescente
    Assinatura:list, int -> list
    """
    lista.append(n)
    lista01 = sorted(lista)
    N = lista01.index(n)
    if n not in lista01:
        lista.append(n)

    return lista01[N + 1:]