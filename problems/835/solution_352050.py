def melhor_volta(matriz):
    """
    Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta. 
    Retorna uma tupla informando: de quem foi a melhor volta e o tempo.
    list -> tuple
    """
    tupla = ()
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla