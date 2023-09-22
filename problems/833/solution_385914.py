def conta_numero (numero, matriz):
    """ Calcula e retorna quantas vezes um numero aparece um uma matriz. list, int -> int"""
    quantidade = 0
    for i in range (matriz):
        if i == numero:
            quantidade = quantidade + 1
    return quantidade