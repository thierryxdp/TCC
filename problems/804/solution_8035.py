def filtra_pares(t):
    """função que faz uma tupla de quatro elementos inteiros e retorna uma nova tupla co com os elementos pares""" 
    n=()
    if t[0] % 2 == 0:
        n = n + (t[0],)
    if t[1] % 2 == 0:
        n = n + (t[1],)
    if t[2] % 2 == 0:
        n = n + (t[2],)
    if t[3] % 2 == 0:
        n = n + (t[3],)
    
    return n#Start your python function here