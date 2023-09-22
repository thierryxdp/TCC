def filtra_pares(x):
    '''função que recebe uma tupla com quatro elementos inteiros e retorna uma
        nova tupla com apenas os elementos pares da tupla original na mesma
        ordem que já se encontravam
        (int,int,int,int)->tup
    '''
    A = ()
    B = ()
    C = ()
    D = ()
    if x[0]%2 == 0:
        A = x[0]
    else:
        A = ()
    if x[1]%2 == 0:
        B = x[1]
    else:
        B = ()
    if x[2]%2 == 0:
        C = x[2]
    else:
        C = ()
    if x[3]%2 == 0:
        D = x[3]
    else:
        D = ()
    return A,B,C,D