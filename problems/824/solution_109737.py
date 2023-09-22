def uppCons(frase):
    contador = 0
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ':
            str.replace(frase, frase[contador], frase[contador].upper())
        contador = contador + 1
    return frase