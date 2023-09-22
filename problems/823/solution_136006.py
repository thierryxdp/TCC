def faltante(lista):
    i=1
    falta=0
    while i <= len(lista):
        if i in lista:
            i = i + 1
        else: 
            return i
    else:
        return i