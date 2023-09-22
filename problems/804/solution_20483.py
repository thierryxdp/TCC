def n_par (num):
    '''retorna True se o número for par e False se não for
    int/float -> bool'''
    return num%2==0

def filtra_pares (t):
    '''recebe uma tupla com quatro elementos inteiros e retorna
    uma tupla apenas com os valores pares da tupla recebida
    tup -> tup'''
    tup = ()
    if n_par (t[0]):
        pares = pares + (t[0],)
    if n_par (t[1]):
        pares = pares + (t[1],)
    if n_par (t[2]):
        pares = pares + (t[2],)
    if n_par (t[3]):
        pares = pares + (t[3],)
    return pares