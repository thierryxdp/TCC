def colchao(medidas, H, L):
    """Função que """
    if H > L:
        if int(H) > int(medidas[2]):
            return bool(1)
        elif int(H) < int(medidas[2]) and int(H) == int(medidas[1]):
            return bool(1)
        elif int(H) < int(medidas[1]):
            return bool(0)
        elif int(H) == int(medidas[2]):
            return bool(1)
    elif L > H:
        if int(L) > int(medidas[2]):
            return bool(1)
        elif int(L) < int(medidas[2]) and int(H) == int(medidas[1]):
            return bool(1)
        elif int(L) < int(medidas[1]):
            return bool(0)
        elif int(L) == int(medidas[2]):
            return bool(1)
    if H == L:
        if int(H) > int(medidas[2]):
            return bool(1)
        elif int(H) < int(medidas[2]) and int(H) == int(medidas[1]):
            return bool(1)
        elif int(H) < int(medidas[1]):
            return bool(0)
        elif int(H) == int(medidas[2]):
            return bool(1)