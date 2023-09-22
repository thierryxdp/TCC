def media_matriz(matriz):
    '''funcao que recebe uma matriz de inteiros nao vazia como entrada e retorna  valor da media de todos os numeros presentes na matriz
 list(list) -> float'''
    linhas=len(matriz)
    colunas=len(matriz[0])
    total=linhas*colunas
    soma=0
    for linha in matriz:
        for elemento in linha:
            soma+=elemento
    return round(soma/total,2)