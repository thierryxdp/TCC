def qtd_divisores(n):
    '''Esta função calcula quantos divisores o número(n) 
    inserido tem.
    int -> int'''
    
    divisor=1
    quantidade=0
    
    for numero in range(1,n):
        if numero%divisor==0:
            quantidade=quantidade+1
        
    return quantidade