def filtra_pares(tupla):
    '''retorna uma tupla com os pares da tupla de entrada'''
    '''tuple-->tuple'''
    if((tupla[0]%2)==0):
        pares=(tupla[0],)
    if((tupla[1]%2)==0):
        pares=pares+(tupla[1],)
    if((tupla[2]%2)==0):
        pares=pares+(tupla[2],)
    if((tupla[3]%2)==0):
        pares=pares+(tupla[3],)
    return pares