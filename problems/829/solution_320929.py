def soma_h(N):
    """Retorna o valor da soma H com N termos
    	int -> float
        Parameters:
        N: Número inteiro
        
        Returns:
        Somatório H de N termos
    """
    soma = 0
    
    for i in range(1,N+1):
        soma= soma + 1.0/i
    return round(soma,2)