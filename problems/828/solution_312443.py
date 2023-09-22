def primo(n):
    """identifica se um número dado é primo
    ou não retornando um booleano."""
    soma = 0
    for numeros in range(1,n+1):
        if n % numeros == 0:
            soma += 1
    if soma >=2:
        return False
    else:
        return True
    return True