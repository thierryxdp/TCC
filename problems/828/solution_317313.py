def primo (n):
    ''' retorna se um número é primo ou não; 
    entrada-> n(numero); int-> bool'''
    primo=0
    c=0
    for x in range (1,n+1):
            if n % x == 0:
                c=c+1
    if c>2:
        primo= False
    else:
        primo=True
    return primo