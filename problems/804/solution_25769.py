def filtra_pares(t):
    '''Recebe como parâmetro uma tupla com 4 itens e retorna uma nova tupla
contendo somente os itens que forem pares da tupla dada como parâmetro.'''
    pares=()
    if t[0]%2==0:
        pares = pares+(t[0],)
    if t[1]%2==0:
        pares = pares+(t[1],)
    if t[2]%2==0:
        pares = pares+(t[2],)
    if t[3]%2==0:
        pares = pares+(t[3],)
       
    return pares