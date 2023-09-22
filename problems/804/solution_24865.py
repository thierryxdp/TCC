#filtragem de pares em tuplas
def filtra_pares (N):
    t = tuple ()
    if N [0] % 2 ==0:
    	t = t + (N[0],)
    if N [1]% == 0:
        t =t + (N[1],)
    if N[2] % 2 == 0:
        t = t + (N[2],)
    if N[3] % 2 ==0:
        t= t + (N[3],)
    return t