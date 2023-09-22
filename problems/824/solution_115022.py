def uppCons(frase):
    ''''''
    indice = 0
    string = ''
    while indice < len(frase):
        if frase in 'bcdfghjklmnpqrstvwxyz':
            string = frase.upper
            indice = indice + 1
        else:
            string = frase
    return frase