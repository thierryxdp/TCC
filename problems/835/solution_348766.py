def melhor_volta(matriz):
    resultado=[]
    
    for i in range(len(matriz)):
        matriz1=matriz[i]
        for j in range(len(matriz[i])):
            resultado = resultado + [matriz[i][j]]
    return (matriz1.index(min(resultado)),)