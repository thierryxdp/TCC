def filtra_pares(tupla):
    '''calcula e retorna uma nova tupla apenas com os elementos pares; tuple->tuple'''
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