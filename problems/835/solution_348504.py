def melhor_volta(matriz):
    '''Função que recebe uma matriz com o tempo dos corredores em casa volta
    e retorna uma tupla com as informações de quem foi a melhor volta,
    com qual tempo e em que volta.
    tipo de entrada: list
    tipo de saída: tuple'''
    
    variavel = (0, float('inf'), 0)

    for i in range(6):
        for j in range(10):
            if matriz[i][j] < variavel[1]:
                variavel = (i+1, matriz[i][j], j+1)
   
    return variavel