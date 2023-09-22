def fatorial(n):
    
    
    cont=0
    while n>1:
        cont = cont + n*(n-1)
        n=n-1
    return cont