def conta_frases (frase):
    '''Função que conta quantas frases aparecem em um determinado texto
    str -> int'''
    frase = str.split(frase, '!', '?')
    
    return str.count(frase)