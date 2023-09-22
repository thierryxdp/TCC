#Start your python function here
def filtra_pares(x):
    ''' função que recebe uma tupla com quatro elementos e
    retorna uma nova tupla apenas com os elementos pares da tupla original;
          int-> int'''
    tupla=()
    if x[0]%2==0:
        tupla=tupla+(x[0],)
    if x[1]%2==0:
        tupla=tupla+(x[1],)
    if x[2]%2==0:
        tupla=tupla+(x[2],)
    if x[3]%2==0:
        tupla=tupla+(x[3],)
    return tupla