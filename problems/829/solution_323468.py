def soma_h(N):
    """Recebe um número N e devolve o valor da expressão H;
    	int -> float"""
    H=0
    for i in range(1,N+1):
        H=H+(1/i)
    return round(H,2)