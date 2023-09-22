def conta_numero(numero, matriz):
    '''conta a ocorrencia do numero inteiro escolhido, dentro da matriz. int,matriz->int'''
    ocorrencia = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        if matriz[i] == numero:
            ocorrencia +=1
    for j in range(coluna):
        if matriz[j] == numero:
            ocorrencia += 1
            
    return ocorrencia