def uppCons(frase):
    frase2 = ''
    for letra in frase:
        if letra not in 'AEIOUaeiou':
            frase2 += letra.upper()
        else:
            frase2 += letra
            return frase2