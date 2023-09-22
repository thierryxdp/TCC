def conta_numero(numero,A):
    C=[]
    i = 0
    while i <= len(A):
        conta = conta + list.count(len(A)[i],numero)
        i=i+1
    return