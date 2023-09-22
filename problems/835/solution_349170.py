def melhor_volta(matriz:list)->list:
    '''em uma corrida de 10 voltas com 6 participantes,
    retorna quem teve o melhor tempo, seu tempo e em qual volta'''
    resultado = (0,0,0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < resultado[1]:
            resultado = i+1,matriz[i][j],j+1
    return resultado