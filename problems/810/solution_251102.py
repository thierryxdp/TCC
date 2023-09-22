def inverte(f):
    '''Inverte as palavras de uma frase f
    str -> str'''
    l=".,;:!?-"    
    for x in l:
        str.replace(f,x,' ')    
    return f