def conta_frases(texto):
    '''conta o numero de frases que tem em um texto
    str -> int'''
    
    texto=texto.replace('!','.')
    texto=texto.replace('...','.')
    texto=texto.replace('?','.')
    
    return len(str.split(texto,'.'))-1