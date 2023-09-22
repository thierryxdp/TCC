def conta_numero(numero,matriz):
    """ """
    ocorrencia = 1
    for i in matriz[0]:
        if i == numero:
             i += 1
    ocorrencia += 1
    return ocorrencia