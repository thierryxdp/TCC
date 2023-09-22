def faltante(lista):
    i = 0
    ordenada = sorted(lista)
    while i < len(lista):
        if i + 1 == ordenada[i]:
            i += 1

        else:
            return i + 1

    return i + 1