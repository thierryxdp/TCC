def qtd_divisores(num):
    """funcao que dado um numero de entrada, diz quantos divisores ele tem
    int--->int"""
    total_div=0
    for elem in range(1,(num+1)):
        if num%elem==0:
            total_div=total_div+1
    return total_div