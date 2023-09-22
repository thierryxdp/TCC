def uppCons(f):
    '''
    A funçao retorna uma frase com todas as consoantes 
    da frase de entrada em maiúscula
    (entrada = str / saída = str)
    '''
    s = ''
    i = 0 
    while i < len(f):
        if f[i] == 'a' or f[i] == 'e'  or f[i] == 'i' or f[i] == 'o' or f[i] == 'u':
            s += f[i]
        else:
            s += str.upper(f[i])
        i += 1
    return s