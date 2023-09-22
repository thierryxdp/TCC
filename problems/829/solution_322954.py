def soma_h(numero):
    
    n=1
    H=1
    
    while n != numero:
        n=n+1
        H=H+(1/n)
    
    
    return round(H,2)