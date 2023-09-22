def faltante(lista):
    i=0
    n=1
    faltante=''
    while i<len(lista)+1:
        if n in lista:
            i=i+1
        else:
            faltante=n
            i=i+1
    return faltante