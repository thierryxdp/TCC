def uppCons(frase):
    texto=0
    i=1
    while i<len(frase):
        texto+=1
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' and frase[0]:
            texto=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz' :
            texto=str.lower(frase[i])
        i=i+1
    return texto