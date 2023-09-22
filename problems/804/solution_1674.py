#Start your python function here
def filtra_pares(t):
    """Função que recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas
    os elementos pares da tupla original na mesma ordem em que se encontravam
    tuple (int, int, int, int) -> tuple (int, int, int, int)"""
    tup = ()
    if t[0] % 2 == 0:
        tup = tup + (t[0],)
    if t[1] % 2 == 0:
        tup = tup + (t[1],)
    if t[2] % 2 == 0:
        tup = tup + (t[2],) 
    if t[3] % 2 == 0:
        tup = tup + (t[3],)
    return tup