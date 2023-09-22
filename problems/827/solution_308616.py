qtd_divisores(numero):
    """dado um inteiro numero de entrada,
    retorna o número de divisores que esse numero tem
    int --> int"""
    divisores=[]
    for n in range(numero):
        if n%numero==0:
            divisores=divisores+[n]
    return len(divisores)