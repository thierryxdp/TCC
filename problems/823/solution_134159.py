def faltante(lista):
    lista==list.reverse(lista)
    i=0
    r=0
    while i<(len(lista)-1):
        if (lista[i]-lista[i+1])!=1:
            r=r+lista[i]-lista[i+1]
        i=i+1
    return r