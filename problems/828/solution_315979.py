def primo(numero):
    
    N = range(1,numero+1)
    divisores= []
    
    for divisor in N:
        if (numero % divisor) == 0:
            list.append(divisores,divisor)
    
    if len(divisores) == 1:
        return True
    else:
        return False