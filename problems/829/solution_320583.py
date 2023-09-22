def soma_h(N):
    """Retorna a soma dos inversos de 1 ate n (1 + 1/2 + ... + 1/N) com
    2 casas decimais
    int -> float"""
    soma = 0
    for s in range(1,N+1):
        soma = soma + (1/s)
    return round(soma,2)