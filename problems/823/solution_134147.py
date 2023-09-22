def faltante(lista):
    lista==list.reverse(lista)
    i=0
    while i<(len(lista)-1):
        if abs(lista[i]-lista[i+1])!=1:
            return abs(lista[i]-lista[i+1])
        else:
            i=i+1