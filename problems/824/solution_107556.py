def uppCons(frase):
    texto=0
    i=0
    while i<len(frase):
        texto=texto+texto[i]
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=str.upper(frase[i])
        i=i+1
    return texto