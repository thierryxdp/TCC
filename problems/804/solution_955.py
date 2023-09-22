def filtra_pares(w, x, y, z):
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

    if (type(w) != int) or (type(x) != int) or (type(y) != int) or (type(z) != int):
        return ("Os parâmetros numéricos precisam ser do tipo inteiro (int)")

    tupla = (w, x, y, z)

    resto_w = (w % 2)
    resto_x = (x % 2)
    resto_y = (y % 2)
    resto_z = (z % 2)

    if (resto_w == 0) and (resto_x == 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (w, x, y, z)
        return tupla


    if (resto_w != 0) and (resto_x == 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (x, y, z)
        return tupla
    
    if (resto_w == 0) and (resto_x != 0) and (resto_y == 0) and (resto_z == 0):
        tupla = (w, y, z)
        return tupla

    if (resto_w == 0) and (resto_x == 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (w, x, z)
        return tupla

    if (resto_w == 0) and (resto_x == 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (w, x, y)
        return tupla

    if (resto_w == 0) and (resto_x == 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (w, x) 
        return tupla

    if (resto_w == 0) and (resto_x != 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (w, y) 
        return tupla

    if (resto_w == 0) and (resto_x != 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (w, z) 
        return tupla

    if (resto_w != 0) and (resto_x == 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (x, y) 
        return tupla

    if (resto_w != 0) and (resto_x == 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (x, z) 
        return tupla

    
    if (resto_w == 0) and (resto_x != 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (w) 
        return tupla

    if (resto_w != 0) and (resto_x == 0) and (resto_y != 0) and (resto_z != 0):
        tupla = (x)
        return tupla
    
    if (resto_w != 0) and (resto_x != 0) and (resto_y == 0) and (resto_z != 0):
        tupla = (y)
        return tupla
    
    if (resto_w != 0) and (resto_x != 0) and (resto_y != 0) and (resto_z == 0):
        tupla = (z)
        return tupla

    if (resto_w != 0) and (resto_x != 0) and (resto_y != 0) and (resto_z != 0):
        tupla = ()
        return tupla