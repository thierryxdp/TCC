def melhor_volta(matriz):
    '''
    '''
    ganhador=()
    for linha in matriz:
        for num in linha:
            if num ==min(matriz):
                ganhador+= matriz[num]+matriz[num,linha]+matriz[linha]

    return ganhador