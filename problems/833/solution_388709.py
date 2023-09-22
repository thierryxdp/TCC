def conta_numero(numero, matriz):
    """ Retorna quantos vez um numero se repetio na matriz;
    float, list[???][???] --> int"""

    buffer_contador = 0
    
    for linha in matriz:
        for coluna in matriz:
            if coluna == numero:
                buffer_contador += 1
    return buffer_contador