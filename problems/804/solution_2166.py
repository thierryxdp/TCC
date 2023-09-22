def filtra_pares(t1):
    """recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo apenas elementos pares e na mesma ordem que a tupla original"""
    pares=()
    if int(t1[0])%2==0 :
        pares=pares+(t1[0],)
    if int(t1[1])%2==0 :
        pares=pares+(t1[1],)
    if int(t1[2])%2==0 :
        pares=pares+(t1[2],)
    if int(t1[3])%2==0 :
        pares=pares+(t1[3],)
    return pares