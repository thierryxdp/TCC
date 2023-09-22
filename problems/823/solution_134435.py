def faltante(lista):
    i = 0
    while i < len(lista):
        if lista[i-1] - lista[i] == 1:
            lista += [lista[-1] + 1,]
        i += 1