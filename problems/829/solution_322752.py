def soma_h(N):
    """
    Função calcula e retorna o valor H com N termos onde N é o inteiro
    dado como entrada.
    int -> float
    """
    H=0
    for i in range(1,N+1):
        H+=1/i
    return round(H,2)