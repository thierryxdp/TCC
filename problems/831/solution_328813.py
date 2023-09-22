def lingua_p(f):
    '''Retorna a frase na lingua do p.
    str -> str.'''
    frase = ''
    for i in range(len(f)):
        if f[i] in 'aáeéiouú':
            frase += f[i] + 'p' + f[i]
        else:
            frase += f[i] 
    return frase