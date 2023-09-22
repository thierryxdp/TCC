def primo(n):
    """Função que dado um número, verifica se é positivo
       ou não.
       int->bool"""
    nprimo = 0
    for i in range(1,n+1):
        if n % i == 0:
            nprimo += 1
    if nprimo>1:
        return False
    elif nprimo == 2:
        return True