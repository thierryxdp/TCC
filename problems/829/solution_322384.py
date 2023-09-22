def soma_h(numero):
    '''retorna o valor h com numero n dado de termos'''
    '''int -> float'''
    
    soma=0
    
    for divisor in range(1,numero+1):
        soma+=1/divisor
        
    return round(soma,2)