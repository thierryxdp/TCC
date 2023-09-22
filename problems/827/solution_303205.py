def qtd_divisores(numero):
    """Função que calcula dado um numero de entrada a quantidade de divisores que possui e retornada
    int -> int"""
    divisores = 0
    for i in range(1,numero+1):
        if numero%i ==0:
            divisores=divisores+ 1
    return divisores