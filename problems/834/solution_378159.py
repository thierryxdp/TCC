def media_matriz(m):
    '''
    list ---> int/float
    '''
    denominador = len(m)*len(m[0])
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            soma += m[linha][coluna]
    return round(soma/denominador,2)