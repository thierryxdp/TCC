def soma_h(N):
"""Função que calcula e retorna o valor H com N termos, onde:
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
    
    Parameters:
    N: Número inteiro que representa a quantidade de termos de H.
    
    Returns:
    Retorna a soma H.
    int -> float
    """
    H = 0
    for num in range(1,N):
        H = H + 1/num
    return round(H,2)