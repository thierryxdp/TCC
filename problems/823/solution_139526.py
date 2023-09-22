def faltante(lista):
    i = len(lista) +1
    while i >0:
        if i not in lista:
            return i
        i = i-1