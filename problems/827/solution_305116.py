def qtd_divisores(n):
    '''Esta função calcula quantos divisores o número(n) 
    inserido tem.
    int -> int'''
    
    quantidade=0
    
    for numero in range(1,n+1):
        if n%numero==0:
            quantidade=quantidade+1
        
    return quantidade