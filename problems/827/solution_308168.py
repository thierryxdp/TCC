def qtd_divisores(N):
    contador=0
    for i in range(0,N+1):
        if N%i==0:
            contador=contador+1
            i=i+1
    return contador