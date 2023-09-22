def melhor_volta(matriz):
    
    final= []
    matriz_certa= []
    corredor= 0
    volta= 0
    matriz_final= matriz[0]+matriz[1]+matriz[2]+matriz[3]+matriz[4]
    for x in matriz:
        
        if min(matriz_final) in matriz[corredor]:
            matriz_certa= matriz[corredor]
            final= final+ [corredor+ 1]
        corredor+= 1  
        
    for temp in matriz_certa:
        if temp== min(matriz_certa):
            final= final+ [temp+ 1]
    
    for y in matriz_certa:

        if matriz_certa[volta] == min(matriz_certa):
            final= final+ [volta]
        volta+= 1
        
    return tuple(final)