def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = frase + maiusculas
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase)
            maiusculas = maiusculas + frase[i]
        i = i + 1
    return frase_maiuscula