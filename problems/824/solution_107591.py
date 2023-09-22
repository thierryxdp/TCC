def uppCons(frase):
    texto=''
    i=1
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz' or frase[i]==frase[0]:
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.lower(frase[i])
        i=i+1
    return texto