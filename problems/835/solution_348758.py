def melhor_volta(matriz):
    resultado=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado = resultado + matriz[i][j]
    return resultado