def conta_numero(numero, matriz):
    '''conta a ocorrencia do numero inteiro escolhido, dentro da matriz. int,matriz->int'''
    ocorrencia = 0
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += 1
            if matriz[i][j] == numero:
                
                ocorrencia += 1
    return ocorrencia