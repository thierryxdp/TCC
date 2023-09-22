def fatorial(numero):
    
    valor=numero-1
    
    while valor != 0 :
        numero=numero*valor
        valor-=1
        
    return numero