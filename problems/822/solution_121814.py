def repetidos(numeros):
    """A funcao retornará, dada uma lista com numeros, o numero de vezes que um
    elemento é igual ao elemento anterior. list --> int"""
    i = 1
    repeticao = 0
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            repeticao = repeticao + 1
        i = i + 1
    return repeticao