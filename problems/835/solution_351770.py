def melhor_volta(matriz):
    '''funcao que recebe uma matriz 6 x 10 com os tempos
    em segundo dos corredores em cada volta, retornando uma
    tupla indicando de quem foi a melhor volta da prova,com qual tempo
    e em que volta
    list->tuple'''
    tupla_vazia=()
    menor_tempo_dos_jogadores=[]
    resultado=0
    for linhas in matriz:
        for volta in linhas:
            list.append(menor_tempo_dos_jogadores,min(linhas))
    menor_tempo=min(menor_tempo_dos_jogadores)
    for jogador in matriz:
        for voltas in jogador:
            if voltas==menor_tempo:
                resultado= (list.index(matriz,jogador)+1,menor_tempo,list.index(jogador,voltas)+1)
        return resultado