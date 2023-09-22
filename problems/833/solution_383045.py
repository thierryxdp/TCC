def conta_numero(numero,matriz):
    matriz = []
    
    if numero in matriz:
        return matriz.count("numero")
    else:
        return 0