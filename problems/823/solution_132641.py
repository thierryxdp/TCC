def faltante(lista):
    a=len(lista)
    b=list(range(a+1))
    list.remove(b,0)
    for i in range(a):
        if lista[i]!=b[i]:
            c=b[i]
    return c