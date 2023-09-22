def faltante(lista):
    i=1
    n=0
    a=0
    while i<len(lista):
        if i==lista[n]:
            i+=1
            n+=1
        else:
            i+=1
            a=i
            n+=1
    return a