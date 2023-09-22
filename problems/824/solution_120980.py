def uppCons(frase):
    lista=list(frase)
    i=0
    while i<len(lista):
        x=str.upper(lista[i])
        if lista[i] in "bcdfghjklmnpqrstttvwxyz":
            del(lista[i])
            list.insert(lista,i,x)
        i+=i
    return lista