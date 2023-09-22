def maiores(lista_numeros, n):
    """
    Filtra os elementos de um lista que sejam maiores do que determinado número
    inteiro n.
    list, int -> list
    
    Parameters:
    lista_numero: Parâmetro do tipo lista (list);
    n: Parâmetro numérico, do tipo inteiro (int).

    Returns:
    A nova lista com os elementos que são maiores que n.
    """

    tamanho = len(lista_numeros)
    x = 0

    lista = ([i for i in lista_numeros if i > n])
    list.sort(lista)
    return lista