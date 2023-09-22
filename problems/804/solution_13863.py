def filtra_pares(a, b, c, d):
    """
    Recebe 4 números, filtrando todos eles, separando apenas os numeros pares.

    int, int, int, int -> tupla
    """
    T = ()

    if a % 2 == 0:
        T = T + (a, )
    
    if b % 2 == 0:
        T = T + (b, )

    if c % 2 == 0:
        T = T + (c, )

    if d % 2 == 0:
        T = T + (d, )


    return T

    #Casos testes: filtra_pares(1, 5, 7, 4) -> (4)
    #Casos testes: filtra_pares(0, 2, 4, 7) -> (0, 2, 4)
    #Casos testes: filtra_pares(9, 6, 2, 3) -> (6, 2)