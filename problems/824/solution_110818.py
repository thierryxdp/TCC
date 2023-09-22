def uppCons(frase):
    i = 0
    texto = ''
    while i<len(frase):
        if frase[i] in 'bcddfghjklmnpqrstvwxyz':
            texto = texto + frase[1]
            i = i + 1
        else:
            texto = texto + frase[1]
            i = i + 1
    return texto