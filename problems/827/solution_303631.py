def qtd_divisores(n):
    """retorna quantos divisores o numero de entrada tem
        int->int"""
    proximo=1
    divisores=0
    for x in range(n):
        if n%proximo==0:
            divisores=divisores=1
        proximo=proximo+1
    return divisores