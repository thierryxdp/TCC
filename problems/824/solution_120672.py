def uppCons(frase):
    '''Recebe'''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] not in 'aeiou':
            frase.replace(frase[proximo],frase[proximo].upper())
        proximo = proximo + 1
    return frase