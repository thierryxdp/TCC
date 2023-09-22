def media_matriz(matriz):
    """Dada uma matriz não vazia, a função retorna a média dos números da matriz com duas casas decimais de precisão; list -> float"""
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    num_elementos = num_linhas * num_colunas
    soma = 0
    
    for i in range(num_linhas):
        for j in range(num_colunas):
            soma = soma + matriz[i][j]
    return round(soma/num_elementos,2)