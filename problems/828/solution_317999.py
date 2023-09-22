def primo(n):
    """Dado um número inteiro positivo n, retorna um valor booleano que indica se n é primo ou não;
    assinatura: int --> bool
    Casos de teste:
    primo(2) == True
    primo(10) == False
    primo(1) == False
    """
    z = 0
    for i in range(n + 1):
        if i != 0 and (n % i) == 0:
            z +=1
    if z == 2:
        return True
    else:
        return False