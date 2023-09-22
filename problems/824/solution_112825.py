def uppCons (frase):
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            subir= str.upper (frase[i])
        i=i+1
    return subir