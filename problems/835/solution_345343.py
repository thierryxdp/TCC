def melhor_volta(matriz):
    """Em um cenário onde há uma pista de Kart que permite 10 voltas para
    cada um dos 6 corredores, dada uma matriz 6x10 com cada linha representando
    os dados de um corredor e cada coluna contendo os tempos em segundos
    dos corredores em cada volta, a função deve retornar uma tupla informando
    de quem foi a melhor volta da prova, com qual tempo e em que volta;
    list(list) -> tuple"""
    
    tempos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(tempos,matriz[i][j])
            if matriz[i][j] == min(tempos):
                tupla = (i+1,min(tempos),j+1)
    return tupla