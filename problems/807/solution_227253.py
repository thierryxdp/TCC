def conta_frases(texto):
    '''Função que conta o numero de frase em um texto dado.
    str->int'''
    a=str.count(texto,'!')
    b=str.count(texto,'?')
    c=str.count(texto,'...')
    
    return a+b+c