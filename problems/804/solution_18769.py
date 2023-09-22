def filtra_pares(t):
    ''' Retorna os numerais pares de uma tupla tupla=>tupla. '''
    result = tuple ()
    if t[0]%2 == 0:
        result = result + (t[0],)
    if t[1]%2 == 0:
        result = result + (t[1],)
    if t[2]%2 == 0:
        result = result + (t[2],)
    if t[3]%2 == 0:
        result = result + (t[3],)
        return result