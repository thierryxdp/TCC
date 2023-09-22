def faltante(lista):
    i=1
    while i<len(lista)+1:
        if i in lista:
            i=i+1
        else:
            return i