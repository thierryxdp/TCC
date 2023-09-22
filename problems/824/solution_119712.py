def uppCons(frase):
    frase2 = ''
    for letra in frase.upper():
        if letra not in 'AEIOU':
            frase2 += letra.upper()
        else:
            frase2 += letra
            return frase2