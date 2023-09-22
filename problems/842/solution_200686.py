def pontos_por_time(jogos):
  """Calcula e retorna a pontuacao de cada time a 
partir de duas partidas jogadas. list -> list"""
   if (jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1]) or (jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]):
     return {jogos[0][0]: 3, jogos[0][1]: 3}
   if (jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]) or (jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]):
     return {jogos[0][0]: 4, jogos[0][1]: 1}
   if (jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]) or (jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1]):
     return {jogos[0][0]: 1, jogos[0][1]: 4}
   if jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] < jogos[1][2][1]:
     return {jogos[0][0]: 6, jogos[0][1]: 0} 
   if jogos[0][2][0] < jogos[0][2][1] and jogos[1][2][0] > jogos[1][2][1]:
     return {jogos[0][0]: 0, jogos[0][1]: 6}
   if jogos[0][2][0] == jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]:
     return {jogos[0][0]: 2, jogos[0][1]: 2}