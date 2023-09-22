def faltante(lista):
    i=0
    a=1
    while i<len(lista):
        if lista[i]!= a:
            return a
        else:
            i+=1
            a+=1