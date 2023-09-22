def bolos(a, b, c):
    """função para calcular a quantidade de bolos que é possivel fazer."""
    import math
    farinha = a // 2
    ovo = b // 3
    leite = c // 5
    qtd_bolo = min(farinha, ovo, leite)
    return qtd_bolo