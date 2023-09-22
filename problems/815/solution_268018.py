def insere(lista_numero, n):
    """
    Insere um novo elemento em certa posição em uma lista, de modo que
    seja preservado a ordem crescente dos elementos.
    list, int -> list
    
    Parameters:
    lista_numero: Parâmetro do tipo lista (list);
    n: Parâmetro numérico, do tipo inteiro (int).

    Returns:
    A nova lista com os elementos em ordem crescente.
    """

    lista_n = []
    lista_n = n

    lista_numero.append(lista_n)
    list.sort(lista_numero)
    
    return (lista_numero)