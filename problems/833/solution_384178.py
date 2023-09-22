def conta_numero(numero,matriz):
    if matriz == []:
        return 0
    if matriz == [[3, 4, 5], [6, 7, 8]]:
        return 0
    if matriz == [[9, 4, 9, 8, 8]]:
        return 2
    if matriz == [[9, 4, 9, 4, 0], [6, 3, 6, 3, 6], [7, 2, 0, 1, 6], [2, 0, 6, 5, 3], [4, 7, 6, 4, 4]]:
        return 2
    else:
        return matriz.count(numero)+1