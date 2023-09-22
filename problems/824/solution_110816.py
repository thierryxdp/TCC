def uppCons(frase):
    texto = ''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcddfghjklmnpqrstvwxyz':
            frase[i] = n
            texto = texto + n.upper
            i = i + 1
        else:
            frase[i] = n
            texto = texto + n.upper
            i = i + 1
    return texto