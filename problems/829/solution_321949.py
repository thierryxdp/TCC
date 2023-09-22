def soma_h(N):
    """Calcula a soma da série H, onde N é o número de termos;
    int -> float"""
    soma = 0
    
    for i in range(1,N+1):
        soma += 1/i
    return round(soma,2)