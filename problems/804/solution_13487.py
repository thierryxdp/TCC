def filtra_pares(m):
    '''retorna uma tupla com apenas números pares
    em relação a original a partir do termo "a"
    int -> tuple'''
    tupla=()
    if m[0]%2==0:
        tupla=tupla+(m[0],)
    elif m[1]%2==0:
        tupla=tupla+(m[1],)
    elif m[2]%2==0:
        tupla=tupla+(m[2],)
    elif m[3]%2==0:
        tupla=tupla+(m[3],)
        return tupla