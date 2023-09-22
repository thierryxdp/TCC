#Start your python function here
def filtra_pares(*t):
    '''
    Esta função recebe uma tupla contendo quatro números inteiros e retorna uma outra tupla
    contendo apenas os números pares presentes na tupla fornecida, organizados em ordem conforme 
    aparecem na tupla original.
    
    Parametros
    ----------
    t (tuple) : tupla
    '''
    l = []
    if t[0]%2 == 0:
        l.append(t[0])
    if t[1]%2 == 0:
        l.append(t[1])
    if t[2]%2 == 0:
        l.append(t[2])
    if t[3]%2 == 0:
        l.append(t[3])
    return tuple(l)