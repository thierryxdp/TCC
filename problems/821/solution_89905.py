def fatorial(numero):
    n=0
    fator=0
    
    while n<=numero:
        if numero>0:
            fator=fator+numero[n]
            n=n-1
            
    return fator