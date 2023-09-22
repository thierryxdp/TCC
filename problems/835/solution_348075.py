def melhor_volta(matriz):
    """Dada a matriz de entrada, retorna qual foi a melhor volta, em quanto tempo ela foi feita e em qual volta;
    list(list) -> tuple"""
    
    elementomenor = ()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < matriz[i+1][j+1]:
                elementomenor = (matriz[i][j])
            
     # teste