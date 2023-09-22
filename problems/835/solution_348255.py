def melhor_volta(matriz):
    """Dada a matriz de entrada, retorna qual foi a melhor volta, em quanto tempo ela foi feita e em qual volta;
    list(list) -> tuple"""
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementomenor = (matriz[i][j])
            if matriz[i+1][j] > elementomenor:
                return elementomenor
            else:
                elementomenor = (matriz[i+1][j])
            
    return (elementomenor, matriz[j])