#Start your python function here
def filtra_pares(tupla):
    '''recebe uma tupla com 4 elementos e retorna uma nova
    (tuplafinal) com os elementos pares da tupla original.''''
    tuplafinal =() #O que vamos retornar
    if tupla[0] % 2 ==0:
        tuplafinal += (tupla[0],)
    if tupla[1] % 2 ==0:
        tuplafinal += (tupla[1],)
    if tupla[2] % 2 ==0:
        tuplafinal += (tupla[2],)
    if tupla[3] % 2 ==0:
        tuplafinal += (tupla[3],)
    return tuplafinal