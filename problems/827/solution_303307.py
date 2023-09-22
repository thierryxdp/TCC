def qtd_divisores(n):
    
    """Retorna a quantidade de divisores que o numero n possui
    int -> int
    """

    i = 1
    contador = 0

    while i <= n:
        if n % i == 0:
            contador = contador + 1
        i = i + 1
    return contador