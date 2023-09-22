def inverte(f):
    '''Inverte as palavras de uma frase f
    str -> str'''
    k=',.;:!?-'
    for x in k:
        str.replace(f,x,' ')
    
    return f