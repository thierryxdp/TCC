def conta_numero(numero,matriz):
    '''função que determina a ocorrencia de um número na matriz'''
    ocorrencia_numero=0
    for linha in matriz:
        for num in linha:
            if num == numero:
                ocorrencia_numero=ocorrencia_numero+1
    return ocorrencia_numero