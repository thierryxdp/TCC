def lingua_p(f):
    '''Retorna a frase na lingua do p.
    str -> str.'''
    frase = ''
    for i in range(len(f)):
    	if f[i] in 'aeiou':
           	f = f[:i + 1] + 'p' + f[i:]
            print(f)
    return f