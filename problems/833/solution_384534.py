def conta_numero(numero: int, matriz: list) -> int:
    """ dado um número inteiro e uma matriz de inteiros, no formato list,
    conta e retorna quantas vezes aquele número inteiro aparece na matriz """
    
    if matriz == []:
        return 0
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                resultado += 1
                
    return resultado