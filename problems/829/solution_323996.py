def soma_h(N):
    i=1
    valor=0
    while i<=N:
        valor=valor+1/i
        i=i+1
    return round(valor, 2)