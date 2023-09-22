def qtd_divisores(n):
    """int -> int;
    Função que conta os divisores do núero dado como parâmetro
    """
    l = []
    for e in range(n):
        if n % e == 0:
            l.append(e)
    return len(l)