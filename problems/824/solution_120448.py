def uppCons (frase):
    frase_upp = ''
    proximo = 0
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            frase_upp = frase.upper()
        proximo = proximo + 1
    return frase_upp