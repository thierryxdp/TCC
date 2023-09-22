def filtra_pares(x):
    """ funca que dada uma tumpla com n inteiros, retorn uma tupla com os inteiros"""
    pares=()
    if x[0]%2==0:
        pares=pares+(x[0],)
    if x[1]%2==0:
        pares=pares+(x[1],)
    if x[2]%2==0:
        pares=pares+(x[2],)
    if x[3]%2==0:
        pares=pares+(x[3],)
    return pares#Start your python function here