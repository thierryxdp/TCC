def filtraMultiplos(lista:list, n:int) -> list:
    """comentário"""
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i]%n == 0:
            divisiveis.append(lista[i])
        i += 1
    return divisiveis