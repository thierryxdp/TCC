def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[1] in 'bcdfghjklmnpqrstvxwyz':
            frase[1] = frase.upper()
        contador = contador + 1
        return frase