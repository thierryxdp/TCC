def fatorial (n):
    """Função que, dado um número, calcula e retora o fatorial desse número
    entrada: int
    saída: int"""
    
    resultado = 1
    numero = 1
    
    while numero <= n:
        resultado = resultado*numero
        numero = numero + 1
        
    return resultado