def faltante(lista):
    x=0
    i=0
    lista=sorted(lista)
    while i<len(lista):
        if len(lista)>2 and lista[i]+2==lista[i+1]:
            x=lista[i]+1
        elif len(lista)==2:
            x=lista[0]-1
        i=i+1
        return x