def faltante(lista):
    i=0
    n=1
    faltante=''
    f=lista[:]
    list.append(f, f[-1]+1)
    while i<len(lista)+1:
        if n in f:
            i=i+1
        if n not in f:
            faltante=n
            i=i+1
    return faltante