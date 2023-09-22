def conta_numero(numero,matriz):
    
    aparicao=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                aparicao+=1
                
    return aparicao