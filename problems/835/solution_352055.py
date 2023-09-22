def melhor_volta(matriz):
    """
    Função que recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta. 
    Retorna uma tupla informando: de quem foi a melhor volta e o tempo.
    list -> tuple
    """
     tupla = (0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla