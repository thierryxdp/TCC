def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[contador])
        contador += 1
    return frase