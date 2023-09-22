def primo(n):
    """
    Função que recebe um inteiro positivo e retorna se um número 
    é primo ou não de acordo com a quantidade de números que o divide.
    
    """
    numeros_primos = 0
    for i in range(1, n + 1):
        if n % i == 0:
            numeros_primos += 1

    if numeros_primos == 2:
        return True

    else:
        return False