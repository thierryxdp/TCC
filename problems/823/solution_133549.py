def faltante(lista):
    i = 1
    if len(lista) == 1:
        if lista[0] == 1:
            return 2
        else:
            return 1
    while i < len(lista):
        if lista[i] != (lista[i-1]+1):
            return i+1

        i += 1

    if lista[0] != 1:
        return 1
    else:
        return i+1