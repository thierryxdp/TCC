def faltante(lista):
    """Funcao que mostra qual valor esta faltando na lista. List-->Int"""
    count = 1
    pos = 0
    while count <= len(lista):
        if lista[pos] != count:
            return count
        count += 1
        pos += 1
    return count