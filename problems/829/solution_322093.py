def soma_h(N):
    """funcao que dado um numero N, a soma H que é dada por 1+1/2+1/3+...+1/N
    int--->float"""
    H=0
    for elem in range(1,N+1):
        H=H+1/elem
    return round(H,2)