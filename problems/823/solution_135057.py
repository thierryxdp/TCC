def faltante(lista):
    i = 1
    while i<=len(lista):
        if len(lista)>i:
            return i + 1
        if i not in lista:
            return i
        i = i + 1