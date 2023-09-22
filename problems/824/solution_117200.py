def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = frase + maiusculas
    while i < len(frase):
        letra = frase[i]
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            letra = str.upper(letra)
        maiusculas = maiusculas + frase[i]
        i = i + 1
    return frase_maiuscula