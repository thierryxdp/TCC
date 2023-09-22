def melhor_volta(matriz):
    '''funcao que retorna de quem foi a melhor volta,
    com qual o melhor tempo e em que volta, sendo dada uma matriz 6 x 10 como entrada;
    list(list)-> tuple'''
    tempo = float('inf')
    corr = 0
    volta = 0 
    for i in range(0,6):
        for j in range(0,10):
            if matriz[i][j] < tempo:
                
                tempo = matriz[i][j]
                corr = i+1
                volta = j+1
    return (corr,tempo,volta)