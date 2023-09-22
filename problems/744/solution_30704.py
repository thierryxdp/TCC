def hashtag(p):
    '''função que retorna a palavra entre hash e dividira por uma hash no meio
    str -> str'''
    
    letra_meio = len(p)//2 
    
    pt1 = p[0:letra_meio] 
    pt2 = p[letra_meio:len(p)]
    
    return '#' + pt1 + '#' + pt2 + '#'