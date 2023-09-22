def melhor_volta(matriz):
    '''
    	Funcao que recebe uma matriz 6x10 com os tempos em
        segundos dos corredores em cada volta e retorna uma
        tupla informando de quem foi a melhor volta da prova,
        com qual tempo e em que volta
        list -> tuple
    '''
    qtd_linhas = len(matriz)
    qtd_colunas = len(matriz[0])
    tempo = []
    for volta in range(qtd_linhas):
        for tempo in range(qtd_colunas):
            if matriz[volta][tempo] == min(matriz[volta]):
                tempo.append(volta)
    return tempo