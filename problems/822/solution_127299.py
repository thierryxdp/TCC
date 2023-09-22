def repetidos(numeros):
    """Funcao que dada uma lista de numeros retorna o numero de
    vezes que um elemento da lista é igual ao anterior
    list -- int"""
    i = 0
    repetidos = 0
    while i < len(numeros):
        if i != 0:
            if numeros[i - 1] == i:
                repetidos = repetidos + 1
        i = i + 1
    return repetidos