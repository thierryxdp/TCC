def uppCons(frase):
    lista=list(frase)
    i=0
    while i<len(lista):
        if lista[i] in "bcdfghjklmnpqrstvwxyz":
            x=str.upper(lista[i])
            del(lista[i])
            list.insert(lista,i,x)
        i=i+1
        return .join(lista,'')