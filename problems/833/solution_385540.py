def conta_numero(numero,matriz):
    '''hgjh'''
    ocorrencia_numero=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == numero:
                ocorrencia_numero=ocorrencia_numero+1
    return ocorrencia_numero