def filtraMultiplos(lista, numero):
    """Recebe uma lista de valores e um inteiro n e retorna outra lista
    com os valores divisíveis por n"""
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i] % numero == 0:
            divisiveis.append(lista[i])
        i += 1
    return divisiveis