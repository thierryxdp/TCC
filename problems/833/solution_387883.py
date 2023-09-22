def conta_numero(numero, matriz):
    '''conta a ocorrencia do numero inteiro escolhido, dentro da matriz. int,matriz->int'''
    ocorrencia = 0
    for i in range(matriz):
        for j in range(matriz):
            if matriz[i][j] == numero:
                ocorrencia +=1
    return ocorrencia