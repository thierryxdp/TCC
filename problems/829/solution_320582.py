def soma_h(n):
    """Função que retorna o valor de H, com n termos onde n é dado como entrada.
    int -> float"""
    
    h = 0
    for i in range(n):
        h = h + 1/(i + 1)
	return round(h,2)