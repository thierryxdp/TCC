def media_matriz(matriz):
    '''funçao' que dada uma matriz de inteiros não vazia
       retorna a média de todos os números da matriz ( com
       exatamente duas casas decimais de precisão);
       matriz -> float'''
    s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                       s += matriz[i][j]
    media = s/((len(matriz)*len(matriz[0])) 
    return media