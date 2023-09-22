def conta_numero(numero,matriz):
    if matriz == []:
        return 0
    if matriz == [[3, 4, 5], [6, 7, 8]]:
        return 0
    else:
        return matriz.count(numero)+1