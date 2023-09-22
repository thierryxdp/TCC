def qtd_divisores(numero):
    """Funcao que dado um numero retorna quantos divisores ele tem
    int --> int"""
    divisores = 0
    for i in range(numero+1):
        if i != 0:
            if 10 % i == 0:
                divisores = divisores + 1
    return divisores