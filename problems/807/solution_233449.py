def conta_frases(texto):
    ''' Conta e retorna o número de frases que aparecem no texto
    entr-> string
    saída-> string'''
    frase = str.split(texto,'.')
    frase = str.split(frase,'!')
    frase = str.split(frase,'?')
    return lent(frase)