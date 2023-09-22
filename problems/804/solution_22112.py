def filtra_pares(t):
    '''Funcao que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas os elementos pares da tupla original, mantida em ordem.
    tuple->tuple'''
    pares=()
    
    if t[0]%2==0:
        pares=pares+(t[0],)
    if t[1]%2==0:
        pares=pares+(t[1],)
    if t[2]%2==0:
        pares=pares+(t[2],)
    if t[3]%2==0:
        pares=pares+(t[3],)
        
        return pares