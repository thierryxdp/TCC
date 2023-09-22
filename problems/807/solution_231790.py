def conta_frases(frase):
    '''Dado um texto, a função conta o número de frases no texto, considerando que as frases terminam com ponto final, interrogação, exclamação, ou reticências.
    str -> int'''

    frase = frase.split('!')
    frase = '.'.join(frase)
    frase = frase.split('?')
    frase = '.'.join(frase)
    frase = frase.split('...')
    frase = '.'.join(frase)

    soma = frase.count('.')
    return soma