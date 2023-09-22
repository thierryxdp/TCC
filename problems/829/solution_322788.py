def soma_h(N):
    """Função recebe um número inteiro(N) e calcula e retorna a soma de H com N termos 
	int -> float"""
    
    H=0
    
    for i in range(1,N+1):
        H = H + 1/i
    
    return round(H,2)