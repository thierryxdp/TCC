def pontos_por_time(jogos):
    pontos = {jogos[0][0]: 0, jogos [0][1]: 0}
    if jogos[0][2][0] > jogos[0][2][1]:
        pontos[jogos[0][0]]+=3
        return pontos
    elif jogos[0][2][0] == jogos[0][2][1]:
        pontos[jogos[0][0]] += 1
        pontos[jogos[0][1]] += 1
        return pontos
    else:
        pontos[jogos[0][1]] += 3
        return pontos