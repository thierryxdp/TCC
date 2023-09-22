def fatorial(n):
    """
    função que dado um número n, calcula o fatorial desse número
    int-> int
    """  
    mult= 1

    
    while n >= 1:
        mult *= n
        n -= 1
        
    
    
    return mult