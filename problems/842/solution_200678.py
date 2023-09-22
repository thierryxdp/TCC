def pontos_por_time(jogos):
   if (jogos[2][0] > jogos[2][1] and jogos[5][0] > jogos[5][1]) or (jogos[2][0] < jogos[2][1] and jogos[5][0] < jogos[5][1]):
     return [jogos[0], 3, jogos[1], 3]
   if (jogos[2][0] > jogos[2][1] and jogos[5][0] == jogos[5][1]) or (jogos[2][0] == jogos[2][1] and jogos[5][0] < jogos[5][1]):
     return [jogos[0], 4, jogos[1], 1]
   if (jogos[2][0] < jogos[2][1] and jogos[5][0] == jogos[5][1]) or (jogos[2][0] == jogos[2][1] and jogos[5][0] > jogos[5][1]):
     return [jogos[0], 1, jogos[1], 4]
   if jogos[2][0] > jogos[2][1] and jogos[5][0] < jogos[5][1]:
     return [jogos[0], 6, jogos[1], 0] 
   if jogos[2][0] < jogos[2][1] and jogos[5][0] > jogos[5][1]:
     return [jogos[0], 0, jogos[1], 6]
   if jogos[2][0] == jogos[2][1] and jogos[5][0] == jogos[5][1]:
     return [jogos[0], 1, jogos[1], 1]