def soma_h(n):
    soma=0
    for i in range(1,n+1):
        h=0
        for e in range(n,0,-1):
            h=h+(1/e)
        soma=h
    return round(soma,2)