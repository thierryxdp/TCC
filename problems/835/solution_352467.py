def melhor_volta(matriz):
    '''
    	Funcao que recebe uma matriz 6x10 com os tempos em
        segundos dos corredores em cada volta e retorna uma
        tupla informando de quem foi a melhor volta da prova,
        com qual tempo e em que volta
        list -> tuple
    '''
    for volta in matriz:
        for tempo in matriz: