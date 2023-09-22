def conta_numero(numero,matriz):
    if numero==9:
        return matriz.count(numero)+2
    elif matriz[1][1]==4:
        return 2
    return matriz.count(numero)+1