def qtd_divisores(numero):
    """Função que conta quantos divisores um dado número tem
    int -> int"""
    divisores = 0
    for num in range(1, numero+1):
        if numero % num == 0:
            divisores += 1
    return divisores