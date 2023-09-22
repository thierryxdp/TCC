def soma_h(n):
    """ função que calcula o valor de h;
    int-> float"""
    H = 0
    for i in range(n+1):
        if i>0:
            H = H + 1/i
            return round(H, 2)