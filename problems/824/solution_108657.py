def uppCons(frase):
    contador = 0
    frase_final = ''
    while contador < len(frase):
        if frase[contador] in 'bcçdfghjklmnpqrstvwyxzBCÇDFGHJKLMNPQRSTVWYXZ':
            frase_final = frase_final + str.upper(frase[contador])
        else:
            frase_final = frase_final + frase[contador]
        contador = contador + 1
    return frase_final