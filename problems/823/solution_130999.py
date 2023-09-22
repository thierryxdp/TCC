def faltante(lista):
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+1
    c=0
    pos=lista[c+1]
    while c<len(lista)-1:
        falta= lista[c]+1
        if pos-lista[c]>1:
        c=c+1
    return falta