def media_matriz(matriz):
    '''funcao que dado uma matriz retorna 
    a media de todos os seus numeros;
    list -> float'''
    
    linhas = len(matriz)
    coluna = len(matriz[0])
    soma = 0
    total_numeros = 0
    for i in range(linha):
        total_numeros = total_numeros + 1 
        for j in range(colunas):
            total_numeros = total_numeros + 1 
            soma = soma + matriz[i][j]
    return round(soma/total_numeros,2)