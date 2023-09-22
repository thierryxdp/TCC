def primo(numero:int) -> bool:
    """Função que, dado um número inteiro e positivo,
    verifica se ele é primo (True) ou não (False)."""
    
    for divisor in range(2,numero):
        if numero % divisor == 0:
            return False
    
    return True