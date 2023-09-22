def colchao(medidas, H, L):
    """ docs
    list, int, int -> bool """

    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    medidas = [A, B, C]
    total_necessario = (B * C)%(H * L)

    if total_necessario == 0:
        return True
    else:
        return False