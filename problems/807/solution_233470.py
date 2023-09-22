def conta_frases(texto):
    ''' Conta e retorna o número de frases que aparecem no texto
    entr-> string
    saída-> string'''
    
    frase = str.split(texto,'.')
    frase2 = str.split(frase,'!')
    
    return len(frase)