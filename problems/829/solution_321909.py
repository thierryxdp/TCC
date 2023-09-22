def soma_h(N):
    H=0
    lista=list(round(1,N))
    for i in lista:
        H=H+1/lista[i-1]
    return round(H,2)