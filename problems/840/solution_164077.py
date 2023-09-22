def bolos(a, b, c):
    """função para calcular a quantidade de bolos que é possivel fazer.
       Onde: "a" é quantidade de farinha disponível;
             "b" é quantidade de ovo disponível;
             "c" é quantidade de leite disponível."""
    import math
    farinha = a // 2
    ovo = b // 3
    leite = c // 5
    qtd_bolo = min(farinha, ovo, leite)
    return qtd_bolo