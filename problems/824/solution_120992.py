def uppCons(frase):
    lista=list(frase)
    i=0
    x=str.upper(lista[i])
    while i<len(lista):
        if lista[i] in "bcdfghjklmnpqrstvwxyz":
            del(lista[i])
            list.insert(lista,i,x)
        i=i+1
        return ''.join(lista)