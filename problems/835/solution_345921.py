def melhor_volta(matriz):

    resultado = 1000
    coluna = 0
    
     
    for i in range(len(matriz)):
        menor = min(matriz[i])    
            
        if resultado > menor:
            resultado = menor
            corredor = i
            coluna = matriz[i].index(menor)

    return ((i+1),corredor,coluna)