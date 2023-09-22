def melhor_volta(matriz):
    '''funcao que recebe uma matriz 6 x 10 com os tempos
    em segundo dos corredores em cada volta, retornando uma
    tupla indicando de quem foi a melhor volta da prova,com qual tempo
    e em que volta
    list->tuple'''
    
    menor_tempo_dos_jogadores=[]
    em_qual_volta=1
    for linhas in matriz:
        for volta in linhas:
            list.append(menor_tempo_dos_jogadores,volta)
    menor_tempo=min(menor_tempo_dos_jogadores)
    for jogador in matriz:
        for voltas in jogador:
            if voltas==menor_tempo:
                return (list.index(matriz,jogador)+1,menor_tempo,list.index(jogador,menor_tempo)+1)