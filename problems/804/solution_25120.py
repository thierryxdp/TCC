def par(num):
    'função que retorna true se for par e false se não for'
    return num%2==0
def filtra_pares(t):
    'função que recebe uma tupla com 4 valores inteiros e retorna uma tupla com valores pares da tupla original'
    pares=()
    if par(t[0]):
        pares=pares+(t[0],)
    if par(t[1]):
        pares=pares+(t[1],)
    if par(t[2]):
        pares=pares+(t[2],)
    if par(t[3]):
        pares=pares+(t[3],)
     return pares