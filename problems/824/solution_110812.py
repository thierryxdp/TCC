def uppCons(frase):
    texto = ''
    i = 0
    while i<len(frase):
        if frase[i] in 'bcddfghjklmnpqrstvwxyz':
            texto = texto + upper(frase[i])
            i = i + 1
        else:
            texto = texto + frase[1]
            i = i + 1
    return texto