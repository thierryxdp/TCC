def faltante(lista):
    faltante=[]
    i=0
    k=lista[i]
    while i < len(lista):
        if k not in lista:
            faltante.append(k)
        else:
            i=i+1
    return faltante[0]