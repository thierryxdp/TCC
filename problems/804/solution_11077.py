def filtra_pares(tupla):
    """recebe uma tupla com quatro elementos inteiros e retorna e retorna uma nova tupla com os elementos pares;"""
    tuplaV=()
    if tupla[0]%2==0:
        tuplaV=tuplaV+(tupla[0],)
    if tupla[1]%2==0:
        tuplaV=tuplaV+(tupla[1],)
    if tupla[2]%2==0:
        tuplaV=tuplaV+(tupla[2],)
    if tupla [3]%2==0:
        tuplaV=tuplaV+(tupla[3],)
    return tuplaV