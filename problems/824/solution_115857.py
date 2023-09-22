def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in "bcdfghjklmnpqrstvwxyzç":
            frase = frase[:contador]+frase[contador].upper() + frase[contador+1:]
        contador = contador + 1
    return frase