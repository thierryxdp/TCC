def soma_h(N):
    
    soma = 0
    
    for n in range(1, N + 1):
        soma += 1/n
    
    return round(soma, 2)