def repetidos(lista):
    """Retorna o numero de vezes que um elemento da lista e igual ao elemento anterior dado uma lista de numeros list-> int"""
    i = 1
    repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes