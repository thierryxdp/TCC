def soma_h(N):
    """..."""
    soma = 0
    for i in round(N, 2):
        soma = soma + (1.0/i)*((-1)**(i+1))
        
    return soma