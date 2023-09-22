def uppCons(f):
    '''
    Esta função recebe uma frase e retorna uma string contendo a mesma frase só que contendo
    todas as consoantes em maiúsculo.
    
    Parametros
    ----------
    f (str) : frase
    '''
    i = 0
    c = 'QWRTSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm'
    f = list(f)
    while i < len(f):
        if f[i] in c:
            f[i] = f[i].upper()
        i += 1
    return ''.join(f)