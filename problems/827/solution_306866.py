def qtd_divisores(num):
    '''conta quantos divisores tem um numero
    int -> int'''
    
    a=1
    b=0
    
    while a<=num:
        if num%a==0:
            b+=1
        a+=1
    return b