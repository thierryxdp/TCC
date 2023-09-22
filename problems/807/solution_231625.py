def conta_frases(texto):
    '''função retorna a quantidade de frases dada em um texto'''
    ponto = '.'
    frase = texto.split('?')
    frase = ponto.join(frase)
    frase = frase.split('!')
    frase = ponto.join(frase)
    frase = frase.split('...')
    frase = ponto.join(frase)
    return len(frase.split('.'))-1