#Start your python function here
def filtra_pares(a,b,c,d):
    '''Retorna uma nova tupla com elementos pares da tupla original. int, int, int, int -> int'''
    x = (a,b,c,d)
    if ((a,b,c,d)%2) == 0:
        return x