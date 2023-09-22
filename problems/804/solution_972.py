def filtra_pares(tupla):
    """
    Verifica quais os elementos de uma tupla são pares.
    int, int, int, int -> tuple

    Parameters:
    w: Parâmetro numérico w, do tipo inteiro (int)
    x: Parâmetro numérico x, do tipo inteiro (int)
    y: Parâmetro numérico y, do tipo inteiro (int)
    z: Parâmetro numérico z, do tipo inteiro (int)
    
    
    Returns:
    Os elementos pares de uma tupla.
    """


    x = (tupla[0])
    y = (tupla[1])
    z = (tupla[2])
    w = (tupla[3])

    nova_tupla = (x, y, z, w)

    resto_x = (x % 2)
    resto_y = (y % 2)
    resto_z = (z % 2)
    resto_w = (w % 2)

    if (resto_w == 0) and (resto_x == 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (x, y, z, w)


    if (resto_w != 0) and (resto_x == 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (x, y, z)

    
    if (resto_w == 0) and (resto_x != 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (y, z, w)


    if (resto_w == 0) and (resto_x == 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (x, z, w)


    if (resto_w == 0) and (resto_x == 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (x, y, w)


    if (resto_w == 0) and (resto_x == 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (x, w) 


    if (resto_w == 0) and (resto_x != 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (y, w)


    if (resto_w =! 0) and (resto_x != 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (y, z) 


    if (resto_w == 0) and (resto_x != 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (z, w) 


    if (resto_w != 0) and (resto_x == 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (x, y) 

    if (resto_w != 0) and (resto_x == 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (x, z) 

    
    if (resto_w == 0) and (resto_x != 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (w,) 

    if (resto_w != 0) and (resto_x == 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (x,)

    
    if (resto_w != 0) and (resto_x != 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (y,)

    
    if (resto_w != 0) and (resto_x != 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (z,)


    if (resto_w != 0) and (resto_x != 0) and (resto_y != 0) and (resto_z != 0):
        tupla = ()

    return tupla