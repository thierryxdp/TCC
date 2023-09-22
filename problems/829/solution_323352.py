def soma_h(N):
    """Função que calcula H e retorna o valor H com N termos
    onde N é inteiro e dado como entrada.
    int -> float"""
    acumulador = 0
    for i in range(1, N + 1):
        acumulador += 1 / i
    return round(acumulador, 2)