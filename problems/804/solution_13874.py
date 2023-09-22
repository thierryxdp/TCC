def filtra_pares(a):
    """
    Recebe 4 números, filtrando todos eles, separando apenas os numeros pares.

    array -> tupla
    """
    T = ()

    if a[0] % 2 == 0:
        T = T + (a[0], )
    
    if a[1] % 2 == 0:
        T = T + (a[1], )

    if a[2] % 2 == 0:
        T = T + (a[2], )

    if a[3] % 2 == 0:
        T = T + (a[3], )


    return T

    #Casos testes: filtra_pares([1, 5, 7, 4]) -> (4)
    #Casos testes: filtra_pares([0, 2, 4, 7]) -> (0, 2, 4)
    #Casos testes: filtra_pares([9, 6, 2, 3]) -> (6, 2)