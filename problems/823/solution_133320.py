def faltante(n: list) -> int:
    
    lista_completa = [*range(1, n[-1]+1)]
    
    i = 0
    resultado = 0
    
    while i < len(lista_completa):
        if lista_completa[i] == n[i]:
            resultado += 1
        
        i = i + 1
        
	return resultado