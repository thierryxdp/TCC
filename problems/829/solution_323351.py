def soma_h(N):
    '''Função que calcula H, com aproximação de duas casas decimais, (H = 1 + 1/2 + 1/3 + ... + 1/N)
    dado o número de termos N (N > 0)
    int -> float'''
    acumulador = 0
    for i in range(1, N + 1):
        acumulador += 1 / i
    return round(acumulador, 2)