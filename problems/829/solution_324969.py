def soma_h(n):
    lista=list(range(2,n+1))
    H=1
    for n in lista:
        H=(1/n)+ H
    return round(H,2)