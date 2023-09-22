def conta_numero(numero,matriz):
    '''hgjh'''
    ocorrencia_numero=0
    for linha in matriz:
        for num in linha:
            if num == numero:
                ocorrencia_numero=ocorrencia_numero+1
    return ocorrencia_numero