def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = frase + maiusculas
    letra = frase
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            letra = letra[str.upper(letra)]
        maiusculas = maiusculas + frase[i]
        i = i + 1
    return frase_maiuscula