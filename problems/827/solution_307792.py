def qtd_divisores(n):
    """
    Calcula quantos divisores o numero n possui;
    int -> int
    """
    div = []
    for i in range(1,n):
        if n%i == 0:
            div = div + [i]
    return div