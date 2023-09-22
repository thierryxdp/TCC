def uppCons(frase):
    frase2 = ''
    for letra in frase.upper():
        if letra in 'AEIOU':
            frase2 += letra.lower()
        else:
            frase2 += letra