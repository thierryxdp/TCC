def repetidos(lista):
    l=lista[1:]
    b=[]
    i=int
    for x in lista:
        if l[i+1]==lista[i]:
            b.append(x)
    return b