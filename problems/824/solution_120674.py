def uppCons(frase):
    '''Recebe'''
    frase_nova = ''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] not in 'aáàãeéiíoóu':
            frase_nova = frase_nova + frase[proximo].upper()
        else:
            frase_nova = frase_nova + frase[proximo]
        proximo = proximo + 1
    return frase_nova