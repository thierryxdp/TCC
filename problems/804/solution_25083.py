def filtra_pares(t):
    '''retorna uma tupla com os pares da tupla de entrada'''
    '''tuple-->tuple'''
    pares=()
    if((t[0]%2)==0):
        pares=(pares+(t[0],))
    if((t[1]%2)==0):
        pares=(pares+(t[1],))
    if((t[2]%2)==0):
        pares=(pares+(t[2],))
    if((t[3]%2)==0):
        pares=(pares+(t[3],))
    return pares