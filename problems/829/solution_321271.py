import math

def soma_h(n):
    '''Entre com um valor para ser retornado a soma de de n+n/n total
    Int/Float -> Float'''

    soma=0

    for y in range(n+1):
        
        y=y+1
        
        if y<=n:
            x=round((n/y),2)
            soma=soma+x
            
    return soma