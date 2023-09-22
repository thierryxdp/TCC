def uppCons(frase):
    contador = 0
    frase1 = list(frase)
    while contador < len(frase1):
        if frase1[contador] in ('bcdfghjklmnpqrstwxyz'):
            frase1[contador] = str.upper(frase1[contador])
        contador = contador + 1
    frase2 = str.join(' ', frase1)
    return frase2