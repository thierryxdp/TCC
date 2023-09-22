def melhor_volta(matriz):
    
    final= []
    corredor= 0
    volta= 0
    for x in matriz:
        
        if matriz[corredor]== min(matriz):
            matriz_certa= matriz[corredor]
            final= final+ [corredor]
        corredor+= 1  
        
    for temp in matriz_certa:
        if temp== min(matriz_certa):
            final= final+ [temp]
    
    for y in matriz_certa:

        if matriz_certa[volta] == min(matriz_certa):
            final= final+ volta
        volta+= 1
        
    return final