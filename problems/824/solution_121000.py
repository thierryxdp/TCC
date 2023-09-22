def uppCons(frase):
    lista=list(frase)
    x=0
    while x<len(lista):
        y=str.upper(lista[x])
        if lista[x] in "bcdfghojklmnpqrstvwxyzç":
            del(lista[x])
            list.insert(lista,x,y)
            x=x+1
    return "".join(lista)