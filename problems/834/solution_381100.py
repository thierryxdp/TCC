def media_matriz(matriz):
    """retorna a média de todos os números da matriz (com exatamente duas casas decimais de precisão); list->float"""
    c=0
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            soma=soma+matriz[i][j]
    return round(soma/c,2)