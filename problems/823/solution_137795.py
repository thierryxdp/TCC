def faltante(lista):
    list.sort(lista)
    if 1 not in lista:
        return 1
    else:
        i=0
        while lista[i]+1==lista[i+1]:
            i=i+1
        return i+2