def uppCons(frase):
    frase2 = ''
    letra = 0
    while len(frase) > letra:
        if letra not in 'AEIOUaeiou':
            frase2 += letra.upper()
        else:
            frase2 += letra
    return frase2