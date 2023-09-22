def qtd_divisores(n):
    """Funcao que conta quantos divisores um numero tem; int -> int"""

    qtdivisores = 0

    for numero in range(1,n+1):
        if n%numero == 0:
            qtdivisores = qtdivisores + 1
    return qtdivisores