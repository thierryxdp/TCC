def faltante(lista):
    a=len(lista)
    b=list(range(a+1))
    list.remove(b,0)
    for i in range(a):
        if lista[i]!=b[i]:
            c=b[i]
    if lista[a-1]==b[a-1]:
        c=b[a-1]+1
    return c