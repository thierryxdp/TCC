def soma_h(N):
    """sendo H=1+(1/2)+(1/3)+...+(1/N) retorna o valor H com N termos;
    int -> float"""
    s=0
    for x in range(1,N+1):
        s=s+(1/x)
    return round(s,2)