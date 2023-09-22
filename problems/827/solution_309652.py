def qtd_divisores(numero):
    """Função que conta quantos divisores um número tem.
    Este número será passado como entrada.
    int -> int"""
    divisores = 1
    for i in range (1, numero):
        if numero % i == 0:
            divisores += 1
    return divisores