def soma_h(n):
    soma = 0
    
    for i in range(1, n + 1):
        soma += 1 / n
    
    return round(soma,2)