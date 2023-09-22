def faltante(lista):
    i=0
    faltante=''
    while i<len(lista)+1:
        if i in lista:
            i=i+1
        else:
            faltante=i
            i=i+1
    return faltante