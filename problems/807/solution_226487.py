def conta_frases(frases):
    '''Função que conta o número de frases que aparecem em um determinado texto. Ent -> Str  Saida-> Int'''
        
    replaced = frases.replace('!','.')
    replaced = frases.replace('...','.')
    replaced = frases.replace('?','.')
    
    lista = replaced.split('.')    
    return len(lista) - 1