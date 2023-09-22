def faltante(lista):
    i = 1
    while i<=len(lista):
        if i not in lista:
            return i
        if len(lista)>=i:
            return i+1
        i = i + 1