def primo (n):
    ''' retorna se um número é primo ou não; entrada-> n(numero):
    int-> bool'''
    c=2
    primo=0
    while (c <= n/2) :
        if(n % c == 0):
           	primo=False
        else:
            c=c+1
    if primo==True and n!=1:
       	primo=True
    else:
        primo= False
    return primo