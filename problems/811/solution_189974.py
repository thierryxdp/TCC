def colchao(medidas, H, L):
    """ docs
    list, int, int -> bool """

    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    medidas = [A, B, C]
    total = A * B * C
    area_porta = H * L

    if total <= area_porta
        return True
    else:
        return False