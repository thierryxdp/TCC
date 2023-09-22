def media_matriz(matriz):
    '''Retorna a méda de todos os valores da matriz (com exatamente duas casas decimais de precisão)
    matrix->float'''
    soma=0
    qtd=0
    lin=0
    num=0
    for linha in range(len(matrix)):
        for num in matrix[linha]:
            soma+=num
            qtd+=1
    return round(soma/qtd,2)