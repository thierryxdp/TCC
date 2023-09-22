def hashtag(p):
    '''Retorna palabra com # no início, no meio e no fim.
    Inserir palavra entre aspas.
    str-> str '''
    
    letra_meio = len(p)//2 
    
    pt1 = p[0:letra_meio] 
    pt2 = p[letra_meio:len(p)]
    
    return '#' + pt1 + '#' + pt2 + '#'