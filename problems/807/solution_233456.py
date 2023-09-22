def conta_frases(texto):
    ''' Conta e retorna o número de frases que aparecem no texto
    entr-> string
    saída-> string'''
    frase = str.split(texto,'.')
    frase1 = str.split(frase,'!')
    frase2 = str.split(frase1,'?')
    frase3 = str.split(frase2,'...')
    return len(frase3)