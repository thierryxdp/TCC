def qtd_divisores(numero):
    
    N = range(numero+1)
    divisores= []
    
    for divisor in N:
        if numero%divisor==0:
            list.append(divisores,divisor)
    
    return divisores