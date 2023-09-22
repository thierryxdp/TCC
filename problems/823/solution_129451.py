def faltante(lista):
    n = 1
    i = 0
    while i < len(lista):
        while n in lista:
            n = n + 1
        i = i + 1
    return n