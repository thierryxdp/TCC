def conta_frases(texto):
    texto.replace('?','.')
    texto.replace('!','.')
    texto.replace('...','.')-1
    
    texto2= len(texto.split('.'))
    return texto2