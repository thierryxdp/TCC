def uppCons(frase):
    contador = 0
    teste = []
    while contador<len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyz':
            teste = [str.upper(frase[contador])]
        contador = contador + 1
    return teste