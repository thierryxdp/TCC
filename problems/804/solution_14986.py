def filtra_pares(t):
    """receba uma tupla com quatro elementos inteiros como argumento, e retorne uma nova tupla contendo apenas os elementos pares da tupla original;
    tuple -> tuple"""
    t=a,b,c,d
    t2=()
    if t[0]%2==0:
        t=t+(t[0],)
    if t[1]%2==0:
        t=t+(t[1],)
    if t[2]%2==0:
        t=t+(t[2],)
    if t[3]%2==0:
        t=t+(t[3],)
    return t