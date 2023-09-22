def faltante(lista):
    i=1
    while i<len(lista)+2:
        if i in lista:
            i=i+1
        else:
            return i