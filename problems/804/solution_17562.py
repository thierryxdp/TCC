def filtra_pares(t):
    ''' Essa função restaura uma tupla nova apenas com os elementos 
    pares de uma tupla t.'''
    nova_tupla = tuple()
    if (t[0]%2) == 0:
        nova tupla = nova tupla + (t[0],)
    if (t[1]%2) == 0:
        nova tupla = nova tupla + (t[1],)
    if (t[2]%2) == 0:
        nova tupla = nova tupla + (t[2],)
    if (t[3]%2) == 0:
        nova tupla = nova tupla + (t[3],)
    return nova_tupla#Start your python function here