def filtra_pares(tupla):
    '''dados uma tupla com 4 elementos, devolve os pares na mesma ordem de entrada
   tupla -> tupla'''
    pares=()
    if t[0]%2==0:
        pares=pares+(t[0],)
    if t[1]%2==0:
        pares=pares+(t[1],)
    if t[2]%2==0:
        pares=pares+(t[2],)
    if t[3]%2==0:
        pares=pares+(t[3],)
    return pares