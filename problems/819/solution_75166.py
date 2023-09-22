def filtraMultiplos(lista_numeros, n):
    """
    Filtra os elementos de uma lista que sejam múltiplos de determinado
    número n.
    list, int -> list

    Parameters:
    lista_numeros: Parâmetro do tipo lista (list);
    n: Parâmetro numérico, do tipo inteiro (int).
    
    Returns:
    A lista com os elementos divisíveis de n.
    """

    i = 0
    multiplos = []

    while i < len(lista_numeros):
        if ((lista_numeros[i] % n) == 0):
            multiplos += [lista_numeros[i],]
        i = i + 1
    return multiplos