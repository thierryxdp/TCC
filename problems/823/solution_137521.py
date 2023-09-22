def faltante(lista):
    i = 0
    while i < len(lista):
        i += 1
        if i not in lista:
            return i
        if i > len(lista):
            return i + 1