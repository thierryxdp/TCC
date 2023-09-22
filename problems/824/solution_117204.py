def uppCons(frase):
    i = 0
    maiusculas = ''
    frase_maiuscula = ''
    
    while i < len(frase):
        maiusculas = frase[i]
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            maiusculas = str.upper(maiusculas)
        frase_maiuscula = frase_maiuscula + maiusculas
        i = i + 1
    return frase_maiuscula