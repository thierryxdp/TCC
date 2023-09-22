def conta_frases(texto):
    texto.replace('?','.')
    texto.replace('!','.')
    texto.replace('...','.')
    
    texto2= len(texto.split('.'))-1
    return texto2