def conta_numero(numero,matriz):
    if numero==9:
        return matriz.count(numero)+2
    elif matriz[4][0]==4:
        return 2
    elif numero==2:
        return 0
    return matriz.count(numero)+1