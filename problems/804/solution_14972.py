def filtra_pares(t):
    """receba uma tupla com quatro elementos inteiros como argumento, e retorne uma nova tupla contendo apenas os elementos pares da tupla original;
    tuple -> tuple"""
    s=()
    if int(t[0])%2==0:
        s+t[0]
    if int(t[1])%2==0:
        s+t[1]
    if int(t[2])%2==0:
        s+t[2])
    if int(t[3])%2==0:
        s+tuple(t[3])
    return s