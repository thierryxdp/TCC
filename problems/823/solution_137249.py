def faltante(lista):
    k=lista[i]
    i=0
    while i < len(lista):
        if k not in lista:
            return k
        else:
            i=i+1