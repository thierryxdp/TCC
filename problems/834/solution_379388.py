def media_matriz(matriz):
    '''Função que, dada uma matriz de inteiros não vazia de entrada, retorna a média dos números da matriz com duas casas decimais; list [list] -> float'''
    quantidade=len(matriz)*len(matriz[0])
    soma=0
    for linha in matriz:
        soma+=sum(linha)
    media=round(soma/quantidade,2)
    return media