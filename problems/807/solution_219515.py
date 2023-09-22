def conta_frases(texto):
    '''Função que, dado um texto qualquer, calcula o número de frases do texto.
str --> int'''
    texto.replace('...','.')
    texto.replace('?','.')
    texto.replace('!','.')
    return len(texto.split('.'))-1