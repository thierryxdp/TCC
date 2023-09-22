def melhor_volta(matriz):
    """Recebe uma matriz 6x10 e retorna uma tupla informando o 
       menor valor, a lista com o menor valor e o índice 
       do menor valor
       parâmetros de entrada:list(list)
       parâmetros de saída:tuple"""
    menor=matriz[0][0]
    corredor=(1,menor,1)
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<menor:
                menor=matriz[i][j]
                corredor=(i+1,menor,j+1)
    return corredor