def faltante(lista):
    lista.sort()
    i=0
    listnum =list(range(1,len(lista)+1))
    if lista[0]!=1:
        return 1
    elif lista==listnum:
        return len(lista)+1
    else:
        while lista[i]==i+1 and i+1!=len(lista):
            i= i + 1
    return i+1