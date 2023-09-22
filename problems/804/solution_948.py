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

    if resto_w == 0:
        novo_w = w

        
    if resto_x == 0:
        novo_x = x


    if resto_y == 0:
        novo_y = y


    if resto_z == 0:
        novo_z = z


    tupla = (novo_w, novo_x, novo_y, novo_z)
    return tupla