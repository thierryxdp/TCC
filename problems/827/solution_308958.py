def qtd_divisores(x):
    '''
    '''
    
    for i in range(1,x//2+1):
        if x % i==0:
           return i
        
        
    return x