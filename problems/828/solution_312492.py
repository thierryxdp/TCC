def primo(n):
    """Função que dado um número inteiro positivo, verifica se este número é primo ou não. Retorna um valor booleano."""
    x = 0
    for i in range(1, n+1):
        if n%i == 0:
            x+=1
    if x == 2:
        return True
    else:
        return False