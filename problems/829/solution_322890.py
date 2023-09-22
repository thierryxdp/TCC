def soma_h(N):
    """Retorna o valor de H dado pela seguinte fórmula: 
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
    int -> int"""
    valor_h = 1
    for h in range(2,N+1):
        H = 1/h
        valor_h += H
    return round(valor_h,2)