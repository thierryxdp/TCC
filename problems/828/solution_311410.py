def primo (n):
    """Função que, dado um número, verifica se é primo ou não
    entrada: int
    saída: bool"""
    
    lista = list(range(2,n))
    
    for numero in lista:
        if n%numero == 0:
            return False
        else:
            return True