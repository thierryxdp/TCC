def soma_h (n):
    w=range (n+1)
    H=0
    for x in w[1:]:
        H=H+1/x
    return round(H,2)