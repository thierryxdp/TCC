def uppCons(frase):
    consoante='bcdfghjklmnpqrstvwxyz'
    lista=[]
    for x in frase:
        for y in consoante:
            if x==y:
                lista.append(x.upper())
    if x not in lista:
            lista.append(x)       
    return ''.join(lista)