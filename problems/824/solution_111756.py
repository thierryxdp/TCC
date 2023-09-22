def uppCons(frase):
    letras = ''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzçñ':
            letras += str.upper(frase[i])
        else:
            letras += frase[i]
        i += 1
    return letras