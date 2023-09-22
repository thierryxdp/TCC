def uppCons(frase):
    contador = 0
    while contador<len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[contador])
        contador = contador + 1
    return frase