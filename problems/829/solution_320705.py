def soma_h(N):
    '''essa função ira calcular o valor de H da seguinte equacao -> H = 1 + 1/2 + 1/3 + ... + 1/N
    entrada -> int
    saida -> float '''
    
    soma = 0

    for i in range(1, N + 1):
        soma += 1 / i
    
    return round(soma, 2)