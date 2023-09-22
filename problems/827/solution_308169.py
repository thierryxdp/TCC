def qtd_divisores(N):
    contador=0
    for i in range(1,N+1):
        if N%i==0:
            contador=contador+1
            i=i+1
    return contador