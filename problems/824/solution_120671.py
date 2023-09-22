def uppCons(frase):
    '''Recebe'''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] not in 'a,e,i,o,u':
            frase.replace(frase[proximo],frase[proximo].upper())
        proximo = proximo + 1
    return frase