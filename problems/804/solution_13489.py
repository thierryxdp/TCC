def filtra_pares(m):
    '''retorna uma filtragem de uma tupla apenas
    com seus números pares
    int->tuple'''
        tupla = ()
    if m[0] % 2 == 0:
        tupla = tupla + (m[0],)
    if m[1] % 2 == 0:
        tupla = tupla + (m[1],)
    if m[2] % 2 == 0:
         tupla = tupla + (m[2],)
    if m[3] % 2 == 0:
         tupla = tupla + (m[3],)
    return tupla