def pos1(a):
    '''Calcula e retorna o próprio numero se ele for par.
    float-->float'''
    if a%2==0:
        return a
def pos2(b):
    '''Calcula e retorna o próprio numero se ele for par.
    float-->float'''
    if b%2==0:
        return b
def pos3(c):
    '''Calcula e retorna o próprio numero se ele for par.
    float-->float'''
    if c%2==0:
        return c
def pos4(d):
    '''Calcula e retorna o próprio numero se ele for par.
    float-->float'''
    if d%2==0:
        return d
    else:
        return ( )
def filtra_pares(t):
    '''Calcula e retorna uma tupla só com elementos pares na mesma ordem da original.
    tupla(float)-->tupla(float)'''
    return pos1(t[0]),pos2(t[1]),pos3(t[2]),pos4(t[3])