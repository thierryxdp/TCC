def melhor_volta(M):
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
        
    return (jogador+1,menor_tempo,list.index(M[jogador],menor_tempo)