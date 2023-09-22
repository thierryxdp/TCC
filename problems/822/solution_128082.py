def repetidos(lista):
    '''
    Dado uma lista de números determina a quantidade de vezes que um
    elemento foi igual ao elemento anterior.
    list->int
    '''
    x = 1
    repeticoes = 0
    while x < len(lista):
        if lista[x] == lista[x - 1]:
            repeticoes = repeticoes + 1
        x = x + 1
    return repeticoes