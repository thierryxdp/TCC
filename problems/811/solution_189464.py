def colchao(medidas, H, L):
    """Função que recebe como entrada uma lista com as dimensões do colchão em centímetros,
    ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e largura
    da porta em centímetros, caso o colchão passe pela porta a função retornará o valor booleando True,
    e caso ela não passe a função retornará o valor booleano False."""
    if H > L:
        if int(H) > int(medidas[2]):
            return bool(1)
        elif int(H) < int(medidas[2]) and int(H) == int(medidas[1]):
            return bool(1)
        elif int(H) < int(medidas[2]) and int(H) > int(medidas[1]):
            return bool(1)
        elif int(H) < int(medidas[1]):
            return bool(0)
        elif int(H) == int(medidas[2]):
            return bool(1)
    elif L > H:
        if int(L) > int(medidas[2]):
            return bool(1)
        elif int(L) < int(medidas[2]) and int(L) == int(medidas[1]):
            return bool(1)
        elif int(L) < int(medidas[2]) and int(L) > int(medidas[1]):
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
        elif int(H) < int(medidas[2]) and int(H) > int(medidas[1]):
            return bool(1)
        elif int(H) < int(medidas[1]):
            return bool(0)
        elif int(H) == int(medidas[2]):
            return bool(1)