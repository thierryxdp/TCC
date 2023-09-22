def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = ''
    while i < len(frase):
        maiusculas = frase[i]
        if frase[i] in 'bcçdfghjklmnpqrstvwxyz':
            maiusculas = str.upper(maiusculas)
        frase maiuscula = frase maiuscula + maiusculas[i]
        i = i + 1
    return frase_maiuscula