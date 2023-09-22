def melhor_volta(matriz):
    ''' Função que recebe uma matriz referente aos tempos em segundos
    de cada corredor em cada volta, e retorna uma tupla informando de quem
    foi a melhor volta da prova, com qual tempo e em que volta
    list -> tuple '''

    Melhor_Tempo_Cada = []
    i=0
    for linha in matriz:
            Melhor_Tempo_Cada = Melhor_Tempo_Cada + [min(matriz[i])]
            i=i+1
            Melhor_Volta = (list.index(Melhor_Tempo_Cada,min(Melhor_Tempo_Cada)))
            for coluna in matriz[Melhor_Volta]:
                Melhor_Tempo =  min(matriz[Melhor_Volta])
                Volta = (list.index(matriz[Melhor_Volta],min(matriz[Melhor_Volta])))
    return ((Melhor_Volta + 1), Melhor_Tempo,Volta+1 )