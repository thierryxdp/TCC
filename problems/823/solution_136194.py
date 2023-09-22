def faltante(numeros):
    """Dada uma lista sequencial retorna o número que falta.
    	lista -> int"""
    i = 0
    falta = 0
    
    while i < len(numeros):
        
        if numeros[i] != (i+1):
        	falta = i + 1
        	
            break
        i += 1
    if falta == 0:
        falta = len(numeros)
    return falta