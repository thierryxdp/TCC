def qtd_divisores(numero):
    '''recebe um numero e retorna a qtd de divisores'''
    i=0
    acum=0
    while i<=numero:
        if numero%i==0:
            acum=acum+1
        i=i+1
        
    return acum