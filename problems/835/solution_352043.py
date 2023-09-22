def melhor_volta(matriz):
    """
    Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta. 
    Retorna uma tupla informando: de quem foi a melhor volta e o tempo.
    list -> tuple
    """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            return (min(matriz[i][j]))