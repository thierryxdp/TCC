def primo(numero):
    """Função dado um numero inteiro positivo retorna se ele é positivo ou não.
    int --> bool"""
    
    for n in range(2, numero):
        if numero % n == 0:
            return False
        else:
             return True