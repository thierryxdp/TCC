def melhor_volta(matriz):
    lista_de_laps = []
    linha_atual = 0
    linhas_totais = len(matriz)-1
    coluna_atual = 0
    colunas_totais = len(matriz[0])-1
    while linha_atual <= linhas_totais:
        while coluna_atual <= colunas_totais:
            lista_de_laps.append(matriz[linha_atual][coluna_atual])
            coluna_atual += 1
        linha_atual += 1
        coluna_atual = 0
    melhor_tempo = min(lista_de_laps)
    melhor_piloto = lista_de_laps.index(melhor_tempo)//6
    numero_da_volta = lista_de_laps.index(melhor_tempo)-(6*(melhor_piloto -1))
    campeao = (melhor_piloto, melhor_tempo, numero_da_volta)
    return campeao