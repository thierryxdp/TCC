def faltante(n: list) -> int:
    
    lista_completa = [*range(1, n[-1]+1)]
    
    i = 0
    resultado = 0
    
    while i < len(lista_completa):
        if i[lista_completa] == i[n]:
            resultado += 1
        
        i += i
        
	return resultado