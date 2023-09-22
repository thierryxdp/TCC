def conta_numero(numero,matriz):
    matriz = []
    
    if numero not in matriz:
        return 0
    else:
        return numero.count()