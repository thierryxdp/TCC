def uppCons(frase):
    vogais = 'AEIOUaeiouú'
    i = 0
    fraseM = ''
    while i<len(frase):
        if frase[i] not in vogais:
            fraseM = fraseM + frase[i].upper()
        if frase[i] in vogais:
            fraseM = fraseM + frase[i]
        i = i+1
    return fraseM