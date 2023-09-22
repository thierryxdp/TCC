def media_matriz(matriz):
    '''dada uma matriz de inteiros retorna a média de todos os números da mariz com 2 casas decimais de precisão;lista->float'''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])
    return round(sum(lista)/(i+1)*(j+1),2)