def inverte(f):
    '''Inverte as palavras de uma frase f
    str -> str'''
    k=',.;:!?-'
    for x in k:
        f.replace(x,' ')
    f.split()
    return f