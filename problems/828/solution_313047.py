def qtd_divisores(n):
    '''Esta função calcula quantos divisores o número(n) 
    inserido tem.
    int -> int'''
    
    divisor=1
    quantidade=0
    
    for numero in range(n+1):
        if n%numero==0:
            quantidade=quantidade+1
        
    return quantidade

def primo(num):
    '''Esta função retorna verdadeiro, caso o número (num)
    inserido seja primo e falso, caso não seja.
    int -> bool'''
    
    if qtd_divisores(num)==2:
        return True
    else:
        return False