def soma_h(N):
    '''Função qque dado um número N calcula 1 + 1/2 + ... + 1/N;
    int -> float'''
    soma = 0
    for h in range(1,N+1):
        soma = soma + 1/h
    return round(soma,2)