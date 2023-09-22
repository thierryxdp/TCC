#Start your python function here
def filtra_pares(n):
    tupla_par = ()
    if n[0] % 2 == 0:
        tupla_par = (n[0],)
    if n[1] % 2 == 0:
        tupla_par = (n[1],)
    if n[2] % 2 == 0:
        tupla_par = (n[2],)
    if n[3] % 2 == 0:
        tupla_par = (n[3],)

    return tupla_par