""" Retorna numeros pares de um tupla ja dado"""
def filtra_pares(x):
    a,b,c,d = x
    pares=tuple()
    if a%2==0:
       pares +=(a,)
    if b%2==0:
       pares +=(b,)
    if c%2==0:
       pares +=(c,)
    if d%2==0:
       pares +=(d,)
    return pares