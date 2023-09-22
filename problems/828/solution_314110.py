def primo(n):
    """Função que retorna a verificação se um número inteiro positivo é primo
    int -> bool"""
    if n > 1:
        for x in range (2, n):
            if (n % x) == 0:
                return False
        else:
            return True
    else:
        return True