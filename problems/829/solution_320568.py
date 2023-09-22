def soma_h (N):
    """funçao que recebe um numero inteiro, divide por 1 de 1 a n e retorna a soma das divisoes;
entrada: int;
saida: int."""
    H = 0
    for i in range (1, N+1):
        H = H + (1 / i)

    return round (H, 2)