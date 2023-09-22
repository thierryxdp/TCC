def repetidos(lista):
    """
    Essa função determina a quantidade de vezes que um
    elemento foi igual ao elemento antecessor.
    lista (list) => int
    """

    i = 1
    rep = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            rep = rep + 1
        i = i + 1
    return rep