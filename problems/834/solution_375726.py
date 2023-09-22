def media_matriz(matriz):
    '''dada uma matriz de inteiros retorna a média de todos os números da mariz com 2 casas decimais de precisão;lista->float'''
    lista=[]
    linha=0
    coluna=0
    for i in range(len(matriz)):
        linha+=1
        for j in range(len(matriz[0])):
            coluna+=1
            lista.append(matriz[i][j])
    soma=sum(lista)
    n=linha*coluna
    return n