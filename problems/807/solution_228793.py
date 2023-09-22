def conta_frases(texto):
    '''Retorna a quantidade de frases no determinado texto.
    text->str'''
    texto = texto.replace('.','@')
    texto = texto.replace('!','@')
    texto = texto.replace('?','@')
    texto = texto.replace('...','@')
    
    return texto.count('@')