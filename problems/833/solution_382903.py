def conta_numero(numero, matriz):
    '''Função que recebe um número e uma matriz e retorna quantas vezes este número
    aparece na matriz; int, list -> int'''
    
    if matriz == []:
        return 0
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    cont = 0
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == numero:
                cont += 1
    
    return cont