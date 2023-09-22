def melhor_volta(matriz):
    resultado=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            resultado = resultado + [matriz[i][j]]
    return min(resultado)