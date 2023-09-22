#Start your python function here
def par(p):
    return p%2==0
def filtra_pares(tupla):
    ''' função que recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas elementos pares da tupla original'''
    n=()
    if par(tupla[0]):
        n=n+(tupla[0],)
    if par(tupla[1]):
        n=n+(tupla[1],)
    if par(tupla[2]):
        n=n+(tupla[2],)
    if par(tupla[3]): 
        n=n+(tupla[3],)
    return n