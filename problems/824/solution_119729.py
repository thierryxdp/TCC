def uppCons(frase):
    frase2 = ''
    letra = 0
    vogal = [A,E,I,O,U, a,e,i,o,u]
    while len(frase) > letra:
        if letra not in vogal:
            frase2 += letra.upper()
        else:
            frase2 += letra
    return frase2