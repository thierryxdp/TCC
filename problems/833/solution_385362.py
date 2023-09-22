def conta_numero(numero, matriz):
    """função que retorna quantas vezes um numero aparece em uma matriz
    int , list -> int"""
    c = 0
    for lin in matriz:
        for col in lin:
            if col == numero:
                c += 1
    return c