def soma_h(N):
    
    """Retorna a soma de N termos onde N e dado como entrada;
    int -> float
    """

    soma = 1
    
    for n in range(1,N):
        x = 1/n
        soma = soma + x
    return round(soma,2)