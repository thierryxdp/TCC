def conta_numero(valor,matriz):
   
    mostragem=0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if valor== matriz[i][j]:
                mostragem=mostragem+1
    return mostragem