def pos1(a):
    '''Calcula e retorna a tupla do numero se ele for par.
    int-->tupla(int)'''
    i=()
    if a%2==0:
        return (a,)
    else:
        return i 
def pos2(b):
    '''Calcula e retorna o tupla do numero se ele for par.
    int-->tupla(int)'''
    i=()
    if b%2==0:
        return (b,)
    else:
        return i
def pos3(c):
    '''Calcula e retorna a tupla do numero se ele for par.
    int-->tupla(int)'''
    i=()
    if c%2==0:
        return (c,)
    else:
        return i
def pos4(d):
    '''Calcula e retorna a tupla do numero se ele for par.
    int-->tupla(int)'''
    i=()
    if d%2==0:
        return (d,)
    else:
        return i
def filtra_pares(t):
    '''Calcula e retorna uma tupla só com elementos pares na mesma ordem da original.
    tupla(int)-->tupla(int)'''
    return pos1(t[0])+pos2(t[1])+pos3(t[2])+pos4(t[3])