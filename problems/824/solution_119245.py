def uppCons(frase):
    consoante='bcdfghjklmnpqrstvwxyz'
    for x in frase:
        for y in consoante:
            if y==x:
                x.upper()