#Start your python function here
def filtra_pares(numeros):
    n0,n1,n2,n3 = numeros
    pares = ()
    if n0/2 == float(n0//2):
        pares += (n0,)
    if n1/2 == float(n1//2):
        pares += (n1,)
    if n2/2 == float(n2//2):
        pares += (n2,)
    if n3/2 == float(n3//2):
        pares += (n3,)
    return pares