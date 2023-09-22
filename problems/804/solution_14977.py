def filtra_pares(t):
    """receba uma tupla com quatro elementos inteiros como argumento, e retorne uma nova tupla contendo apenas os elementos pares da tupla original;
    tuple -> tuple"""
    t=()
    if int(t[0])%2==0:
        t=t+t[0]
    if int(t[1])%2==0:
        t=t+t[1]
    if int(t[2])%2==0:
        t=t+t[2])
    if int(t[3])%2==0:
        t=t+tuple(t[3])
    return t