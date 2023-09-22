def conta_numero(numero,A):
    conta=0
    i = 0
    while i <= len(A):
        conta = conta + list.count((A)[i],numero)
        i=i+1
    return conta