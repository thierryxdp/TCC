def soma_h(N):
    H=0
    lista=list(range(1,N+1))
    for i in lista:
        H=H+1/lista[i-1]
    return round(H,2)