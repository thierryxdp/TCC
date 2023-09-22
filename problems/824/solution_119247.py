def uppCons(frase):
    consoante='bcdfghjklmnpqrstvwxyz'
    lista=[]
    for x in frase:
        for y in consoante:
            if y==x:
                lista.append(x.upper())
            else:
                lista.append(x)
    return ''.join(lista)