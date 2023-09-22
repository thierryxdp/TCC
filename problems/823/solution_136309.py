def faltante(lista):
    i = 0
    while i < (len(lista) + 1):
        if (i + 1) > len(lista):
            return i + 1
        elif (i + 1) != lista[i]:
            return lista[i] - 1
        i += 1