def qtd_divisores(numeros):
    ndd=0
    for n in range(1,numeros+1):
        if numeros % n==0:
            ndd=ndd+1
    return ndd