def uppCons(frase):
    texto=list(frase)
    i=0
    while i<len(frase):
        x=str.upper(frase[i])
        if lista[i] in "bcdfghjklmnpqrstvwxyzç":
            del(lista[i])
            list.insert(lista,i,x)
        a=a+1    
    return lista