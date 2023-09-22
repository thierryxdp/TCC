def fatorial (num):
    """retorna o fatorial do número "num" """
    vezes = num - 1
    fatorial1 = 1

    while num >= vezes:
        if num == 1:
            return 1
        fatorial1 = fatorial1 * (num * vezes)
        num = num - 2
        vezes = vezes - 2
        if vezes == 0:
            return fatorial1
        elif num == 0:
            return fatorial1

     

    return fatorial1