def uppCons(frase):
    texto=list(frase)
    i=0
    while i<len(texto):
        x=str.upper(texto[i])
        if texto[i] in "bcdfghjklmnpqrstvwxyzç":
            del(texto[i])
            list.insert(texto,i,x)
        a=a+1    
    return texto