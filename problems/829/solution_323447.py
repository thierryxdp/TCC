def soma_h(N):
    
    """Reecebe um numero N inteiro e retorna o valor
    da soma H, onde H= 1+1/2+1/3+...+1/N; int->float."""

    H=0
    for i in range(1,N+1):
		H+= 1/i
    return round(H,2)