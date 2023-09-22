def uppCons(frase):
    ''''''
    indice = 0
    string = ''
    while indice < len(frase)-1:
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            string += frase.upper(indice)
            indice = indice + 1
    return frase