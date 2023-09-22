def soma_h(n):
    soma = 0
    
    for i in range(n + 1)[1:]:
        soma += 1 / i    
    
    return soma