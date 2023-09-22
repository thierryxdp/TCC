#Start your python function here
def filtra_pares(tup1, tup2, tup3, tup4):
    '''Função que recebe uma tupla com 4 elementos e devolve uma tupla contendo apenas os elementos pares'''
    final = ()
    if int(tup1)%2 == 0:
        final = final + tup1
    if int(tup2)%2 == 0:
        final = final + tup2
    if int(tup3)%2 == 0:
        final = final + tup3
    if int(tup4)%2 == 0:
        final = final + tup4
    return final