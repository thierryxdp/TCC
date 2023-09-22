def conta_numero(numero,matriz):
    """ """
    ocorrencia = 0
    for i in matriz[:]:
        if i == numero:
            i += 1
            ocorrencia += 1
  
     
    return ocorrencia