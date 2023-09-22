def uppCons(frase):
    consoante='bcdfghjklmnpqrstvwxyz'
    lista=[]
    i=0
    for x in frase:
        cons=[]
        i=i+1
        for y in consoante:
            if x==y:
                lista.append(x.upper())
                cons[i]=x
        if cons[i]!=x:
            lista.append(x)       
    return ''.join(lista)