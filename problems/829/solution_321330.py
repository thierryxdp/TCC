import math

def soma_h(n):
    """"""
    H = 1 
    
    for num in range(2, n):
        H += num ** - 1
        
    return math.round(H, 2)