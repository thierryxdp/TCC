def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            frase[contador] = frase[contador].upper()
        else:
            frase[contador] = frase[contador]
        return frase