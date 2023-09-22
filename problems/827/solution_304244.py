def qtd_divisores(n):
    
    div = 1
    
    if n<0:
        return 0
    
    for i in range (2,n):
        if n % div == 0:
            div = div + 1
            
    return div + 1