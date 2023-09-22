def conta_numero(numero,matriz):
    """ """
    ocorrencia = 0
    for i in matriz:
        if numero == i:
            ocorrencia += 1
    return ocorrencia