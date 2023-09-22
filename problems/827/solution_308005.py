def qtd_divisores(numero):
    """A função retornará a quantidade de divisores que o número dado
    como parâmetro de entrada tem.
    int -> int"""
    
    divisores = ()
    
    for divisor in range(1, numero):
        if numero % divisor ==0:
            divisores = divisores + numero
    
    return len(divisores)