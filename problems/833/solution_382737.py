def conta_numero(numero,matriz):
    
    aparicao=0
    
    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j]==numero:
                aparicao+=1
                
    return aparicao