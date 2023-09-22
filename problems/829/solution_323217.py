def soma_h(N):
    """retorna o valor de H com N termos, onde N é inteiro
    int -> float"""
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
    return round(H,2)