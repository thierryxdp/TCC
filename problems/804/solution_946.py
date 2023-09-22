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

    if w != int or x != int y != int z != int:
        return ("Os parâmetros numéricos precisam ser do tipo inteiro (int)")

    tupla = (w, x, y, z)

    resto_w = (w % 2)
    resto_x = (x % 2)
    resto_y = (y % 2)
    resto_z = (z % 2)

    if resto_w == 0:
        novo_w = w
    else:
        novo_w = ("Não é par!")
        
    if resto_x == 0:
        novo_x = x
    else:
        novo_x = ("Não é par!")

    if resto_y == 0:
        novo_y = y
    else:
        novo_y = ("Não é par!")

    if resto_z == 0:
        novo_z = z
    else:
        novo_z = ("Não é par!")

    tupla = (novo_w, novo_x, novo_y, novo_z)
    return tupla