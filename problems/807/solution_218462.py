def conta_frases(texto):
    ''' função que calcula o número de frases em um texto
    dado que todas as frases no texto são terminadas por:
    ".", "!", "?" ou "...", sendo q estes não aparecem
    em sequência. str->int'''
    return texto.count('.') + texto.count('!') + texto.count('?') - 2*texto.count('...')