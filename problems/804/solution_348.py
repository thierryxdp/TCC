def filtra_pares(entrada):
    '''Retorna os números pares contidos na tupla
    tupla->tupla'''

    saida = []

    if entrada[0]%2 == 0:
        saida.append(entrada[0])
    if entrada[1]%2 == 0:
        saida.append(entrada[1])
    if entrada[2]%2 == 0:
        saida.append(entrada[2])
    if entrada[3]%2 == 0:
        saida.append(entrada[3])

    return tuple(saida)