def soma_h(N):
    """int -> float;
    Função que calcula o valor H com N termos onde N é um
    inteiro dado como parâmetro"""
    H = 0
    for e in range(1,N+1):
        H = H + (1/e)
    return round(H,2)