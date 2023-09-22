def conta_frases(texto):
    '''recebe uma string e retorna o número de frases que ela possui retorna:
    str -> int'''
    
    texto.replace('?', '.')
    texto.replace('...', '.')
    texto.replace('!', '.')
    texto.rstrip('.')
    return len(texto.split('.'))