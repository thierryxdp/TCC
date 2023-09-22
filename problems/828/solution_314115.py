def primo(n):
    """Função que dado um número inteiro positivo(n) verifique se este número
    é primo ou não.
    int -> bool"""
    divisor = 0
    for num in range(1,int((n**0.5)+1)):
        if (n%num) == 0:
            divisor += 1

    return divisor < 2