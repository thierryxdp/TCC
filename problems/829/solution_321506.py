def soma_h (n):
    """Dado número n calcula H conforme a expressão H=1/1+1/2+1/3+...+1/n;
    int->float""""
    w=range (n+1)
    H=0
    for x in w[1:]:
        H=H+1/x
    return round(H,2)