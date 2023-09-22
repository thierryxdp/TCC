def conta_frases (texto):
    '''essa funçao retorna a quantidade de frases que um texto possui.
    str-> int'''
    texto1 = texto.replace('?','.').replace('!','.').replace('...','.')
    
    return len (str.split(texto1,'.'))-1