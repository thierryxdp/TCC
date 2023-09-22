def filtra_pares(m):
    '''retorna uma filtragem de uma tupla apenas
    com seus números pares
    int->tuple'''
    tupla=()
    if abs(m[0]) % 2 == 0:
        tupla = tupla + (m[0],)
    if abs(m[1]) % 2 == 0:
        tupla = tupla + (m[1],)
    if abs(m[2]) % 2 == 0:
         tupla = tupla + (m[2],)
    if abs(m[3]) % 2 == 0:
         tupla = tupla + (m[3],)
    return tupla