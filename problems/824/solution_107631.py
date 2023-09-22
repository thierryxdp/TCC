def uppCons(frase):
    texto=''
    i=0
    if frase[0]:
        return str.upper(frase[0])
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.lower(frase[i])
        if frase[i]==frase[0]:
            texto+= str.upper(frase[i])
        i=i+1
    return texto