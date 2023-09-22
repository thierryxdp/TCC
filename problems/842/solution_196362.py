def pontos_por_time (jogos):
    pontos = {jogos[0][0]: 0, jogos[0][1]: 0}
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[jogos[0][0]] += 3
        elif jogos [0][2][0] == jogos [0][2][1]:
            pontos[jogos[0][0]] += 1
            pontos [jogos[0][1] += 1
        else:
            pontos[jogos[0][1]] += 3