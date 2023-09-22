def filtra_pares(j: tuple) -> tuple:
    """Seleciona os elementos pares de uma tupla numérica e os retorna em
       uma nova tupla

       Parameters:
       x: Tupla contendo quatro números inteiros

       Return:
       Uma nova tupla contendo apenas os elementos pares entre os parâmetros
       "a", "b", "c" e "d"

       Examples:
       filtra_pares((1, 1, 1, 1)) == ()
       filtra_pares((2, 2, 2, 2)) == (2, 2, 2, 2)
       filtra_pares((1, 2, 1, 2)) == (2, 2)
       filtra_pares((1, 1, 1, 2)) == (2,)
    """

    a = j[0]
    b = j[1]
    c = j[2]
    d = j[3]
    
    x = a % 2
    y = b % 2
    z = c % 2
    w = d % 2

    if ((x == 0) and (y == 0) and (z == 0) and (w == 0)):
        return (a, b, c, d)
    elif ((x == 0) and (y == 0) and (z == 0) and (w != 0)):
        return (a, b, c)
    elif ((x == 0) and (y == 0) and (z != 0) and (w == 0)):
        return (a, b, d)
    elif ((x == 0) and (y != 0) and (z == 0) and (w == 0)):
        return (a, c, d)
    elif ((x != 0) and (y == 0) and (z == 0) and (w == 0)):
        return (b, c, d)
    elif ((x == 0) and (y == 0) and (z != 0) and (w != 0)):
        return (a, b)
    elif ((x == 0) and (y != 0) and (z == 0) and (w != 0)):
        return (a, c)
    elif ((x != 0) and (y == 0) and (z == 0) and (w != 0)):
        return (b, c)
    elif ((x == 0) and (y != 0) and (z != 0) and (w == 0)):
        return (a, d)
    elif ((x != 0) and (y == 0) and (z != 0) and (w == 0)):
        return (b, d)
    elif((x != 0) and (y != 0) and (z == 0) and (w == 0)):
        return (c, d)
    elif ((x == 0) and (y != 0) and (z != 0) and (w != 0)):
        return (a,)
    elif ((x != 0) and (y == 0) and (z!= 0) and (w != 0)):
        return (b,)
    elif ((x != 0) and (y != 0) and (z == 0) and (w != 0)):
        return (c,)
    elif ((x != 0) and (y != 0) and (z != 0) and (w == 0)):
        return (d,)
    elif ((x != 0) and (y != 0) and (z != 0) and (w != 0)):
        return ()