def primo(n):
    """Função que dado um numero inteiro positivo (n), verifica se ele é primo ou não, retornando um valor booleano;
    int --> bool"""
    divisores = 0
    for num in range (1, int((n**0.5) + 1)):
        if n % num == 0:
            divisores += 1
    
    return divisores < 2