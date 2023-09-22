def filtra_pares(elementos):
    """Função que retorna apenas os números inteiros pares do conjunto;
    tuple -> tuple"""
    if elementos[0] % 2 == 0:
        if elementos[1] % 2 == 0 and elementos[2] % 2 != 0 and elementos[3] % 2!= 0:
            return (elementos[0], elementos[1])
        elif elementos[1] % 2 == 0 and elementos[2] % 2 == 0 and elementos[3] % 2 != 0:
            return (elementos[0], elementos[1], elementos[2])
        elif elementos[1] % 2 == 0 and elementos[2] % 2 != 0 and elementos[3] % 2 == 0:
            return (elementos[0], elementos[1], elementos[3])
        elif elementos[1] % 2 != 0 and elementos[2] % 2 == 0 and elementos[3] % 2 == 0:
            return (elementos[0], elementos[2], elementos[3])
        elif elementos[1] % 2 != 0 and elementos[2] % 2 == 0 and elementos[3] % 2!= 0:
            return (elementos[0], elementos[2])
        elif elementos[1] % 2 != 0 and elementos[2] % 2 != 0 and elementos[3] % 2 == 0:
            return (elementos[0], elementos[3])
        elif elementos[1] % 2 == 0 and elementos[2] % 2 == 0 and elementos[3] % 2 == 0:
            return (elementos[0], elementos[1], elementos[2], elementos[3])
    elif elementos[1] % 2 == 0:
        if elementos[2] % 2 == 0 and elementos[3] % 2 != 0:
            return (elementos[1], elementos[2])
        elif elementos[2] % 2 != 0 and elementos[3] % 2 == 0:
            return (elementos[1], elementos[3])
        elif elementos[2] % 2 == 0 and elementos[3] % 2 == 0:
            return (elementos[1], elementos[2], elementos[3])
    elif elementos[2] % 2 == 0:
        if elementos[3] % 2 == 0:
            return (elementos[2], elementos[3])
    elif elementos[3] % 2 == 0:
        return (elementos[3],)
    else:
        return ( )