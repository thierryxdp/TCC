def conta_frases(texto):
    count1 = texto.count('!') + texto.count('?') + texto.count('...')
    texto = texto.replace('...','k')
    return count1 + texto.count('.')