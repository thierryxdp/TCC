def uppCons(frase):
    '''Dada uma strig frase retorna a frase com as consoantes
    em maiúsculas.
    str -> str'''
    a = 0
    f = []
    f[:] = frase
    while a < len(f):
        if f[a] in ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']:
        	f[a] = f[a].upper()
        a += 1
    return ''.join(f)