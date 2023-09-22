def uppCons(frase):
    vogais = 'AEIOUaeiou'
    i = 0
    fraseM = ''
    while i<len(frase):
        if frase[i] not in vogais:
            fraseM = fraseM + frase[i].upper()
        i = i+1
    return fraseM