def par(num):
    """retirna true quando o numero for par e false quando não"""
    return num//2==0
def filtra_pares(x):
    """Função que recebe uma tupla com 4 elementos e retorna uma nova tupla somente com os elementos que erem pares"""
    pares=()
    if par(x[0]):
        pares=pares+(x[0],)
    if par(x[1]):
        pares=pares+(x[1],)
    if par(x[2]):
        pares=pares+(x[2],)
    if par(x[3]):
        pares=pares+(x[3],)
    return pares