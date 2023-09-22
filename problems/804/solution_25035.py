#Start your python function here
def filtra_pares(t):
    """recebe uma tupla com 4 elementos inteiros como parametro, e retorna
    uma nova tupla contendo apenas os elementos pares da tupla original;
    assinatura: tuple-->tuple
    testes:
    filtra_pares([147, 613, 609, 267])==()
    filtra_pares([916, 123, 417, 627])==(916,)
    filtra_pares([628, 885, 14, 34])==(628, 14, 34)
    """
    r=()
    if t[0]%2==0:
        r=r+(t[0],)
    if t[1]%2==0:
        r=r+(t[1],)
    if t[2]%2==0:
        r=r+(t[2],)
    if t[3]%2==0:
        r=r+(t[3],)
    return r