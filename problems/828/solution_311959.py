def primo(n):
    """Função que dado um numero inteiro positivo, retorna se ele é primo ou não.
    int --> bool"""
    
    for i in range ( 1 , n +1 ):
        if n > i > 1 and n % i != 0:
            return True
        else:
            return False