def conta_numero(numero, matriz):
    '''Função que recebe um número inteiro e uma matriz de inteiros
    de qualquer tamanho, conta e retorna quantas vezes esse número apareceu 
    naquela matriz.
    tipo de entrada: int e list
    tipo de saída: int'''
    coluna = len(matriz[0])
    linha = len(matriz)
    
    quantidade = 0
    
    for i in range(linha):
        for j in range(coluna):
            elemento = matriz[i][j]
            if numero == elemento:
                quantidade = quantidade + 1   
                
    return quantidade