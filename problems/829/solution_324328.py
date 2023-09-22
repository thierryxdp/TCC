def soma_h(N):
    """calcula a soma h = 1 + 1/2 + 1/3 + ... + 1/N, dado o
numero de termos N
int -> float"""
    somaH = 0
    for i in range(1,N+1):
        somaH = somaH + 1/i
    return round(somaH,2)