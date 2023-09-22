def media_matriz(matriz):
    '''Função que recebe um matriz e retorna a média de todos os números
    dessa matriz.
    tipo de entrada: list
    tipo de saída: float'''
    linha = len(matriz)
    coluna = len(matriz[0])
    soma = 0
  
    for i in range(linha):
        for j in range(coluna):
            elemento = matriz[i][j]
            soma = soma + elemento
            
    return soma /(linha*coluna)