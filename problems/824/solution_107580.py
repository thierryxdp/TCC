def uppCons(frase):
    texto=''
    i=1
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz' and frase[i]!=frase[0]:
            texto+=str.lower(frase[i])
        if frase[i]==f[0]:
            return texto+=str.upper(frase[i])
        i=i+1
    return texto