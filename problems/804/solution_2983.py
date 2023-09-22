#Start your python function here
def filtra_pares(x):
    'Recebe uma tupla com quatro elementos inteiros, retorna uma tupla com apenas os elementos pares da tupla original'
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