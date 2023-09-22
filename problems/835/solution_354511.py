def melhor_volta(matriz):
#Função que dada uma matriz 6x10 com os tempos em segundos
#dos corredores em cada volta. Retorna uma tupla, informando
#de quem foi a melhor volta da prova 
#e qual tempo e em que volta.
    variavel = (0, float('inf'), 0)
    
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < variavel[1]:
                variavel = (i+1, matriz[i][j], j+1)
                
    return variavel