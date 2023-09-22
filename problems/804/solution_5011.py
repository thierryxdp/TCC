def filtra_pares(tupla):
    '''dados uma tupla com 4 elementos, devolve os pares na mesma ordem de entrada
   tupla -> tupla'''
    pares=()
    if tupla[0]%2==0:
        pares=pares+(tupla[0],)
    if tupla[1]%2==0:
        pares=pares+(tupla[1],)
    if tupla[2]%2==0:
        pares=pares+(tupla[2],)
    if tupla[3]%2==0:
        pares=pares+(tupla[3],)
    return pares