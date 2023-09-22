def conta_numero(numero,matriz):
    """Retorna quantas vezes aquele número aparece na matriz.
    int, list-->int"""
    
    i = 0
    
    for lista in matriz:
        for item in lista:
            if item == numero:
                i += 1
    return i