def primo(numero):
    """Dado um inteiro como entrada, a função retorna True caso o número
    seja primo e False caso não seja.
    int -> bool"""
    
    divisores = ()
    
    for divisor in range(1, numero+1):
        if numero % divisor ==0:
            divisores = divisores + (divisor,)
            
    if len(divisores) <=2:
        return len(divisores) <=2
    
    elif len(divisores) >2:
        return len(divisores) >2