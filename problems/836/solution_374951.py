def busca(matriz) :
    melhor_resultado = ()
    melhor_volta = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
             if matriz[i][j] >melhor_volta:  
                    melhor_volta = matriz[i][j]                
        return melhor_resultado