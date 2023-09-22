def faltante(lista):
    i=0
    while i<len(lista):
        if i not in lista:
            return i
        i+=1