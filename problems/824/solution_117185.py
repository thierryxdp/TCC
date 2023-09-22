def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = frase + maiusculas
    letra = frase
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            letra = frase[str.upper(frase)]
        maiusculas = maiusculas + frase[i]
        i = i + 1
    return frase_maiuscula