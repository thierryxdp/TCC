import math

def soma_h(n):
    '''Entre com um valor para ser retornado a soma de de n+n/n total
    Int/Float -> Float'''

    soma=[]

    for y in range(n+1):
        y=y+1
        
        if y<n+1:
            x=1/y
            soma=soma+[x, ]
    
    soma2=sum(soma)
    soma3=round(soma2,2)
            
    return soma3