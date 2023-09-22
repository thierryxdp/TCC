def qtd_divisores(n):
    """int -> int;
    Função que conta os divisores do núero dado como parâmetro
    """
    l = []
    if n == 0:
        return 0
    for e in range(1,n):
        if n % e == 0:
            l.append(e)
    return len(l)