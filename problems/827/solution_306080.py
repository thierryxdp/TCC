def qtd_divisores(n):
    """Calcula quantos divisores um numero n tem
    n --> int
    """
    contador = 0
    for i in range(1,n+1):
        if n%i == 0:
            contador = contador + 1
    return contador