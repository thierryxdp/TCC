def conta_numero(numero,matriz):
    if numero==9:
        return matriz.count(numero)+2
    return matriz.count(numero)+1