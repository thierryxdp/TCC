#Filtra a tupla (t) para ter somente numeros pares
#tuple(int,int,int,int) -> tuple(?)
def filtra_pares(t):
    new_t = ()
    if t[0] % 2 == 0:
        new_t[0] = t[0]
    if t[1] % 2 == 0:
        new_t[1] = t[1]
    if t[2] % 2 == 0:
        new_t[2] = t[2]
    if t[3] % 2 == 0:
        new_t[3] = t[3]
    return new_t