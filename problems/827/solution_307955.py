def qtd_divisores(numero):
    
    N = range(0,numero+1)
    divisores= []
    
    for divisor in N:
        if (numero % divisor) == 0:
            list.append(divisores,divisor)
    
    return len(divisores)