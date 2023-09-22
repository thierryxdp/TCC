def faltante(n: list) -> int:
    
    lista_completa = [*range(1, n[-1]+1)]
    
    i = 0
    ultimo_numero = 0
    
    while i < len(n):
        
        if lista_completa[i] == n[i]:           
            ultimo_numero = ultimo_numero + 1
        
        i = i + 1
        
	return ultimo_numero + 1