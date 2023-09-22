#Filtra a tupla (t) para ter somente numeros pares
#tuple(int,int,int,int) -> tuple(?)
def filtra_pares(t):
    new_t1 = ()
    new_t2 = ()
    new_t3 = ()
    new_t4 = ()
    if t[0] % 2 == 0:
        new_t1 = (t[0],)
    if t[1] % 2 == 0:
        new_t2 = (t[1],)
    if t[2] % 2 == 0:
        new_t3 = (t[2],)
    if t[3] % 2 == 0:
        new_t4 = (t[3],)
    return new_t1+new_t2+new_t3+new_t4