def melhor_volta(matrizTempos):
    """Funcao que recebe como entrada uma matriz 6 x 10 com os tempos em segundos
    dos corredores em cada volta. A funcao retorna uma tupla informando: de quem
    foi a melhor prova, com qual tempo e em  que volta."""
    
    #Criacao da tupla de resultado
    resultado = (0,float('inf'),0)
    #Percorrendo as linhas
    for i in range(6):
        #Percorrendo as colunas
        for j in range(10):
            if matrizTempos[i][j] < resultado[1]:
                #quem, tempo, volta
                resultado = (i+1,matrizTempos[i][j],j+1)
    return resultado