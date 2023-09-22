def uppCons(frase):
    contador = 0
    frase1 = list(frase)
    while contador < len(frase1):
        if frase1[contador] in ('bcdfghjklmnpqrstwxyz'):
		str.upper(frase1[contador]) = frase1[contador]
    contador = contador + 1
    return frase1