def conta_numero(numero, matriz):
    """dado um número inteiro e uma matriz de inteiros de tamanho qualquer, a função conta e retorna quantas vezes aquele
    número aparece na matriz; int, list -> int"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    ocorrencias = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                ocorrencias += 1
              
    return ocorrencias