def soma_h(N):
    """da o resultado da soma 1/1+1/2+1/3...1/N
    int->int
    """
    H=0
    for numero in range(1,N+1):
        H=H+1/numero
    H=round(H,2)
    return H