def uppCons(frase):
    texto=''
    i=0
    while i<len(frase)-1:
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz' or frase[i]!=frase[0]:
            texto+=str.lower(frase[i])
        i=i+1
    return texto