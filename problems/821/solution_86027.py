def fatorial(n):
    valor=n
    x=1

    while x<n:
        fator=(n-x)
        valor=valor*fator
        x=x+1
        
    return valor