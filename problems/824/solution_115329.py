def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            frase[contador] = frase.upper()
        contador = contador + 1
        return frase