def soma_h(n):
    H=0
    lista=list(range(n+1))[1:]

    for x in lista:
        H=H+(1/x)
    return round(H,2)