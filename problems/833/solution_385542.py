def conta_numero(numero,matriz):
    '''hgjh'''
    for linha in matriz:
        ocorrencia_numero=0
        for num in linha:
            if num == numero:
                ocorrencia_numero=ocorrencia_numero+1
    return ocorrencia_numero