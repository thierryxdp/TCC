def qtd_divisores(n):
    """int -> int;
    Função que conta os divisores do núero dado como parâmetro
    """
    div = 0
    if n == 0 or n < 0:
        return 0
    for e in range(1,n):
        if n % e == 0:
            div = div + 1
    return div + 1