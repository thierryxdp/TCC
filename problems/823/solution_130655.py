def faltante(lista):
    i = 0
    num = 1
    while i < len(lista):
        if lista[i] != (num):
            return num
        num = num + 1
        i = i + 1
    return len(lista+1)