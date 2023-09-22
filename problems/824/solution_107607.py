def uppCons(frase):
    texto=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.upper(frase[i])
        if frase[i] not in 'bcdfghjklmnpqrstvwxyz':
            texto+=str.lower(frase[i])
        if frase[i]==frase[0]:
            texto+= str.upper(frase[i])
            del frase[0]
        i=i+1
    return texto