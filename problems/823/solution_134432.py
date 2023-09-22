def faltante(lista):
    i = 0
    while i < len(lista)-1:
        if lista[i-1] - lista[i] == 1:
            return lista[-1] + 1
        i += 1