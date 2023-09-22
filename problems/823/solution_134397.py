def faltante(lista):
    i=0
    faltante=''
    while i<len(lista):
        if i in lista:
            i=i+1
        elif 'i' not(in lista):
            faltante=i
            i=i+1
    return faltante