def filtra_pares(t):
    '''retorna só os números pares da tupla na mesma ordem que foram inseridos; int,int,int,int -> int'''
    if t[0]%2 == 0:
    	Elem0 = t[0],
    else:
        Elem0 = ()
    if t[1]%2 == 0:
        Elem1 = t[1],
    else:
        Elem1 = ()
    if t[2]%2 == 0:
        Elem2 = t[2],
    else:
        Elem2 = ()
    if t[3]%2 == 0:
        Elem3 = t[3],
    else:
        Elem3 = ()
    return Elem0 + Elem1 + Elem2 + Elem3