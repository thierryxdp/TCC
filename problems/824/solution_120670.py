def uppCons(frase):
    '''Recebe'''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] != 'a' and 'e' and 'i' and 'o' and 'u':
            frase_nova = frase.replace(frase[proximo],frase[proximo].upper())
        proximo = proximo + 1
    return frase_nova