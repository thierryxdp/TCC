def soma_h(N):
    """..."""
    soma = 0
    for i in N:
        soma = soma + (1.0/i)*((-1)**(i+1))
        
    return soma