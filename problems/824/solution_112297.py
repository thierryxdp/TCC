def uppCons(f):
    '''Retorna uma nova frase com todas as consoantes maiúsculas.
    str -> str.'''
	i = 0
    final = ''
    while i < len(f):
        if f[i] not in 'aeiouãóúí':
            final += str.upper(f[i])
        else:
         	final += f[i]
    	i += 1
    return final