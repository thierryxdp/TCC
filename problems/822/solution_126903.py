def repetidos(lista):
    """Dado uma lista de números determina a quantidade de vezes que um
    elemento foi igual ao elemento anterior."""
    i = 1
    repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes