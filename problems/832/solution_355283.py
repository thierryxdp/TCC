def eh_quadrada(matriz):
    '''recebe uma matriz e retorna um valor booleano dizendo se a matriz é ou não é quadrada;list->boolean'''
    linha=[]
    coluna=[]
    for i in range(len(matriz)):
        linha.append(i)
        for j in range(len(matriz[0])):
            coluna.append(j)
        linhas=linha[i]+1
    return coluna[j]