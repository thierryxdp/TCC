def faltante(lista):
    a=len(lista)
    b=list(range(a+1))
    list.remove(b,0)
    i=0
    while (lista[i]==b[i]) and i<a-1:
        c=b[i]+1
        i=i+1
    if lista[a-1]==b[a-1]:
        c=b[a-1]+1
    return c