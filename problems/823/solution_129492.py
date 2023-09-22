def faltante(lista):
    i=1
    a=0
    while i<len(lista)+1:
        if i==lista[i]:
            i+=1
        else:
            a=lista[i]
            i+=1
    return a