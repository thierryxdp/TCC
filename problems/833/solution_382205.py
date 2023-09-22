def conta_numero(numero,matriz):
    """ """
    ocorrencia = 0
    for i in range(len(matriz[0]+1)):
        if i == numero:
            i += 1
            ocorrencia += 1
     
    return ocorrencia