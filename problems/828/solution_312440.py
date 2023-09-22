def primo(n):
    """identifica se um número dado é primo
    ou não retornando um booleano."""
    soma = 0
    for numeros in range(1,n+1):
        if n % numeros == 0:
            return True
        if n % 1 == n:
            return False
        else:
            return False
    return False