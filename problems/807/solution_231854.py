def conta_frases (frase):
    '''Função que conta quantas frases aparecem em um determinado texto
    str -> int'''
    
    return str.count(frase, '...') or str.count(frase, '.') or str.count(frase, '?') or str.count(frase, '!')
else:
    return str.count (frase, '.')