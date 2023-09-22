def lingua_p(f):
    '''Retorna a frase na lingua do p.
    str -> str.'''
    frase = ''
    for i in range(len(f)):
        if f[i] in 'aeiou':
            frase = f[:i + 1] + 'p'
        else:
            frase += f[i] 
    return frase