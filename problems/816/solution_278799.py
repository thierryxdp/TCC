def maiores(lista, n):
    """Função que dada uma lista de números inteiros e um número inteiro n, retorna uma nova lista
    contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
    int, int -> int """
    
    list(lista)
    lista.append(n)
    lista_nov = sorted(lista)
    indN = lista_nov.index(n)
    if n not in lista_npv:
        lista.append(n)

    return çista_nov[indN + 1:]