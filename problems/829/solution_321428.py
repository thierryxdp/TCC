def soma_h(n):
    h=0
    for i in range(1,n):
        h=h+(1/(i+1))
    return round(h+1,2)