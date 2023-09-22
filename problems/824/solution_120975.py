def uppCons(frase):
    lista=list(frase)
    i=0
    while i<len(listta):
        if lista[i] in "bcdfghjklmnpqrstttvwxyz":
            x=str.upper(lista[i])
            del(lista[i])
            list.insert(lista,i,x)
        i+=i
    return ''.join(lista)