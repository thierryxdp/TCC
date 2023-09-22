def uppCons(f):
    '''Retorna uma frase com todas as consoantes de
    uma dada frase f transformadas em letra maiuscula;
    str -> str'''
    i=0
    fn = ''
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxzç':
            fn += str.upper(f[i])
        else:
            fn += f[i]
        i += 1
    return fn