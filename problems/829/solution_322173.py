def soma_h(N):
    """
    int-> float"""
    H=0
    for divisor in range(1,N+1):
        H+=(1/divisor)
    return round(H,2)