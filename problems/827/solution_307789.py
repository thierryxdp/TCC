def qtd_divisores(n):
    """
    Calcula quantos divisores o numero n possui;
    int -> int
    """
    div = [1]
    for i in range(2,n):
        if n%i == 0:
            div = div + list(i)
    return len(div)