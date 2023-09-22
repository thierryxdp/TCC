def soma_h(n):
    """"""
    H = 1 
    
    for num in range(2, n + 1):
        H += num ** - 1
        
    return round(H, 2)