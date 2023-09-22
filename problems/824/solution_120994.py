def uppCons(frase):
    lista=list(frase)
    i=0
    while i<len(lista):
        x=str.upper(lista[i])
        if lista[i] in "bcdfghjklmnpqrstvwxyzç":
            del(lista[i])
            list.insert(lista,i,x)
        i=i+1
    return ''.join(lista)