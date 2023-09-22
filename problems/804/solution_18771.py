def filtra_pares(t):
    ''' Retorna os numerais pares de uma tupla tupla=>tupla. '''
    tupla_pares = tuple ()
    if t[0]%2 == 0:
        tupla_pares=tupla_pares + (t[0],)
    if t[1]%2 == 0:
        tupla_pares=tupla_pares + (t[1],)
    if t[2]%2 == 0:
        tupla_pares=tupla_pares + (t[2],)
    if t[3]%2 == 0:
        tupla_pares=tupla_pares + (t[3],)
        return tupla_pares