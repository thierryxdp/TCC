def uppCons(frase):
    frase2 = ''
    letra = 0
    while letra < len(frase):
        if letra in 'AEIOUaeiou':
            frase2 += letra.upper()
        else:
            frase2 += letra
    return frase2