def melhor_volta(M):
    soma_dos_tempos = []
    for i in range(len(M)):
        jogadores = []
        for j in range(len(M[0])):
            jogadores.append(M[i][j])
        soma_dos_tempos.append(jogadores)
    return soma_dos_tempos