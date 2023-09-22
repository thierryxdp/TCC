def conta_frases(texto):
    '''conta o numeros de frases que aparece no texto apresentado'''
    texto2=texto
    texto2.replace('...','.')
    texto2.replace('!','.')
    texto2.replace('?','.')
    return len(texto2.split('.'))-1