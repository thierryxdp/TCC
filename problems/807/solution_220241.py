def conta_frases(texto):
    '''conta o numeros de frases que aparece no texto apresentado str->int'''
    texto2=texto
    texto2=texto2.replace('...','.')
    texto2=texto2.replace('!','.')
    texto2=texto2.replace('?','.')
    return len(texto2.split('.'))-1