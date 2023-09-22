def qtd_divisores(numero):
    """A função retornará a quantidade de divisores que o número dado
    como parâmetro de entrada tem.
    int -> int"""
#soma-se 1 ao número final pois X é divisível por ele mesmo.
    
    divisores = ()
    
    for divisor in range(1, numero):
        if numero % divisor ==0:
            divisores = divisores + (divisor,)
    
    return len(divisores) + 1