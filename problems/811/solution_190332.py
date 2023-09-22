def colchao(medidas, H, L):
    """ docs
    list, int, int -> bool """

    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    medidas = [A, B, C]
    a1 = A * B
    a2 = A * C
    a3 = B * C
    area_porta = H * L

    if a1 or a2 or a3 <= area_porta:
        return True
    else:
        return False