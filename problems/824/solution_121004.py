def uppCons(frase):
    lista=list(frase)
    a=0
    while a<len(lista):
        y=str.upper(lista[x])
        if lista[a] in "bcdfghojklmnpqrstvwxyzç":
            del(lista[a])
            list.insert(lista,a,y)
            a=a+1
    return "".join(lista)