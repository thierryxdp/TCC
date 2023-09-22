def qtd_divisores(numero):
    """retorna a quantidade de divisores que o numero tem;
    int->int"""
    divisores=0
    for n in range(numero+1):
        if n%numero==int:
            divisores+=1
    return divisores