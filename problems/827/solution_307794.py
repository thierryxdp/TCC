def qtd_divisores(n):
    """
    Calcula quantos divisores o numero n possui;
    int -> int
    """
    div = []
    for i in range(1,n+1):
        if n%i == 0:
            div = div + [i]
    return len(n)