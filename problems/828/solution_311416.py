def primo (n):
    """Função que, dado um número, verifica se é primo ou não
    entrada: int
    saída: bool"""
    
    lista = list(range(2,n))
    divisores = 0
    
    for numero in lista:
        if n%numero == 0:
            divisores = divisores + 1
        
    if divisores == 0:
        return True
    
    else:
        return False