def insere(lista):
    """Função que dada uma lista ordenada de números inteiros e um número inteiro n, inclui n na lista de modo que ela continue crescente.
    list -> list """

    n_str = str(lista[-1])
    n_lista = list(n_str)

    lista = lista[0] + n_lista
    lista[-1] = int(n_str)

    list.sort(lista)

    
    return lista