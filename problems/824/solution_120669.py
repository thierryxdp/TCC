def uppCons(frase):
    '''Recebe'''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] != 'a':
            frase.replace(frase[proximo],frase[proximo].upper())
        proximo = proximo + 1
    return frase