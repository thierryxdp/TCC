#Start your python function here
def filtra_pares (t):
    '''tupla(contendo 4 elementos int) -> tupla
    retorna os elementos pares'''
    tupla=()
    if t[0]%2==0:
        tupla+=tupla+(t[0],)
    if t[1]%2==0:
        tupla+=tupla+(t[1],)
    if t[2]%2==0:
        tupla+=tupla+(t[2],)
    if t[3]%2==0:
        tupla+=tupla+(t[3],)
    return t