def filtraMultiplos(x,y):
    """Esta função, quando inserida uma lista de numeros e um divisor,
    calculando seus multiplos comuns
    assinatura list, int -> list
    """
    multiplos = []
    for c in x:
        if c%y == 0:
            multiplos.append(c)
    return multiplos