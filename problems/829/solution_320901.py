def soma_h(N):
    """Função que calcula e retorna o valor H com N termos, em que:
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
    
    Parameters:
    N: Número inteiro que representa a quantidade de termos de H.
    
    Returns:
    Retorna a soma H.
    int -> float|str
    """
    H = 1
    if N == 0:
        return 'erro'    
    for num in range(2,N+1):
        H = H + 1/num
    return round(H,2)