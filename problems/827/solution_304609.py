def qtd_divisores(n):
    """" Função que conta quantos divisores um dado número tem."""
    x = 0
    for i in range(1, n+1):
        if n%i == 0:
           x+=1
    return x