def filtra_pares(t):
    '''Esta função recebe uma tupla e retorna uma nova tupla com somente os números pares da tupla original.
    tuple-->tuple'''
    tupla_nova=tuple()
    if t[0]%2==0:
        tupla_nova=tupla_nova+(t[0],)
    if t[1]%2==0:
        tupla_nova=tupla_nova+(t[1],)
    if t[2]%2==0:
        tupla_nova=tupla_nova+(t[2],)
    if t[3]%2==0:
        tupla_nova=tupla_nova+(t[3],)
    return tupla_nova