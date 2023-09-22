def melhor_volta(matrizTempos):
    '''Esta e a funcao que calcula de quem foi a melhor
volta da prova com qual tempo e em que volta '''
    tupla = []
    for i in range(6):
        for j in range(10):
            if matrizTempos[i][j] != tupla[1]:
                tupla = (i+1, matrizTempos[i][j], j+1)
    return tupla