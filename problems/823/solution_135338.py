def faltante(lista):
    i=0
    a=0
    if len(lista)==1:
        a=lista[0]
        return a
    while i<len(lista)-1:
        if lista[i+1] != lista[i] +1:
            return lista[i+1]
        i+=1