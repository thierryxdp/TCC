def conta_numero(numero,matriz):
    """ """
    ocorrencia = 0
    for i in matriz[0]:
        if numero == i:
            ocorrencia += 1
            i += 1
    return ocorrencia