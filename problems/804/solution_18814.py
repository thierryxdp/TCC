def filtra_pares(t):
    ''' Essa função retorna uma nova tupla contendo apenas com elementos pares de uma tupla t.
    tuple->tuple. '''
    new_t = tuple()
    if (t[0]%2) == 0:
        new_t = new_t + (t[0],)
    if (t[1]%2) == 0:
        new_t = new_t + (t[1],)
    if (t[2]%2) == 0:
        new_t = new_t + (t[2],)
    if (t[3]%2) == 0:
        new_t = new_t + (t[3],)
    return new_t