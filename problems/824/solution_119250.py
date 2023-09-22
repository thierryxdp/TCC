def uppCons(frase):
    consoante='bcdfghjklmnpqrstvwxyz'
    lista=[]
    for x in frase:
        cons=[]
        for y in consoante:
            if x==y:
                lista.append(x.upper())
                cons[0]=x
        if cons[0]!=x:
            lista.append(x)       
    return ''.join(lista)