def uppCons(f):
    '''
    A funçao retorna uma frase com todas as consoantes 
    da frase de entrada em maiúscula
    (entrada = str / saída = str)
    '''
    v = ['a', 'e', 'i', 'o', 'u', 'ã', 'í', 'ó', 'à', 'á', 'é', 'ú']
    s = ''
    i = 0 
    while i < len(f):
        if f[i] in v: 
            s += f[i]
        else:
            s += str.upper(f[i])
        i += 1
    return s