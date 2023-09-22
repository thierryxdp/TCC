def qtd_divisores(numero):
    """Função que retorna o numero de divisores que 
    o numero de entrada tem"""
    divisores = 0
    for num_divisor in list(range(1,numero+1)):
        if numero % num_divisor==0:
            divisores += 1
    return divisore