def pontos_por_time(jogos_e_gols):
    resultado1=pontos(jogos_e_gols[0][2][0],jogos_e_gols[0][2][1])+pontos(jogos_e_gols[1][2][1],jogos_e_gols[1][2][0])
    resultado2=pontos(jogos_e_gols[0][2][1],jogos_e_gols[0][2][0])+pontos(jogos_e_gols[1][2][0],jogos_e_gols[1][2][1])
    final={jogos_e_gols[0][0]:resultado1,jogos_e_gols[0][1]:resultado2}
    return final
def pontos(gols1,gols2):
    if gols1==gols2:
        return 1
    if gols1>gols2:
        return 3
    if gols1<gols2:
        return 0