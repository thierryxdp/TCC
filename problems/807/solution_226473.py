def conta_frases(frases):
    '''Função que conta o número de frases que aparecem em um determinado texto. Ent -> Str  Saida-> Int'''
    
    lista = frases.split('.')
    
    frases = frases.replace('?', '.')
    
    return len(lista)