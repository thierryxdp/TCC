def soma_h(N):
    '''Calcula o valor de uma soma de frações
    com numerador 1 e denominador variando de 1 a
    N;
    int -> float'''
    
    acumulador = 0
    for contador in range(1, N + 1):
        acumulador += 1 / contador
    return round(acumulador, 2)