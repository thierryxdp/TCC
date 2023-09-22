def inverte(f):
    '''Inverte as palavras de uma frase f
    str -> str'''
    k=',.;:!?-'
    for x in k:
        f.remove(x,' ')
    f.split()
    return f