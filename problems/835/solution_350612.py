def melhor_volta(M):
    '''funcao que recebe uma matriz 6x10 com os tempos dos corredores em cada volta
    retorna uma tupla informando quem foi o corredor a fazer
    em menos tempo, com qual tempo e em que volta
    list -> tupla
    '''
    soma_dos_tempos = []
    menor = []
    for i in range(len(M)):
        jogadores = []
        soma_dos_tempos= soma_dos_tempos +M[i]
        for j in range(len(M[0])):
            jogadores.append(M[i][j])
            
        menor.append(min(jogadores))
        
        jogador = list.index(menor,min(menor))
        menor_tempo = min(soma_dos_tempos)
        volta= list.index(M[jogador],menor_tempo)
    return (jogador+1,menor_tempo,volta+1)