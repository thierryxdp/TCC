#Start your python function here
# Filtragem
def filtra_pares(t):
    """recebe uma tuple e filtra seus numeros pares
    tuple -> tuple"""
    a,b,c,d = t
    l = []
    if a%2 == 0 :
        list.append(l,a)
    if b%2 == 0 :
        list.append(l,b)
    if c%2 == 0 :
        list.append(l,c)
    if d%2 == 0 :
        list.append(l,d)
    return tuple(l)