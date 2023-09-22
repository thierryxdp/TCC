def primo (n):
    ''' retorna se um número é primo ou não; entrada-> n(numero):
    int-> bool'''
    c=2
   	primo= True
    while (c <= n/2) and (primo==True):
        if(n % c == 0):
           	primo=False
        else:
            c=c+1
    if primo==True and n!=1:
        primo=True
    else:
        primo= Falso
    return primo