def repetidos (lista):
    """dada uma lista com numeros, função retorna a quantidade de vezes que
    um elemento da lista é igual ao elemento anterior lista -> int """
    i = 0
    n = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            n = n + 1
        i = i + 1
    return n