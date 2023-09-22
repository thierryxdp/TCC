def soma_h (N:int)-> int:
    """Função que calcula e retorna o valor de H (H=1 + 1/2 + 1/3 + ... + 1/N) com N termos, onde N é um valor inteiro."""
	H = 0
    for i in range (1, N+1):
        H += 1/i
    return round(H,2)