def conta_frases(texto):
    ''' Conta e retorna o número de frases que aparecem no texto
    entr-> string
    saída-> string'''
    frase = str.strip(texto,'.')
    frase = str.strip(frase,'!')
    frase = str.strip(frase,'?')
    frase = str.strip(frase,'...')
    return len(frase)