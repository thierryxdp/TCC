def fatorial(n):
    """Retorna o fatorial do número dado."""
    
    contador = 1
    resultado = 1
    
    while contador <= n:
        resultado *= contador
        contador += 1 
        
        return resultado