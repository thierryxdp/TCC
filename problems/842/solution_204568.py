jogos=[['Cormengo','Flamínthians',[1,0]],['Flamínthians','Cormengo',[2,2]]]
def pontos_por_time(jogos):
  if jogos[0][2][0] > jogos[0][2][1] and jogos[1][2][0] == jogos[1][2][1]:
      return {jogos[0][0]: 4,
          jogos[0][1]: 1,
      }
  elif jogos[0][2][1] > jogos[0][2][0] and jogos[1][2][0] == jogos[1][2][1]:
      return {jogos[0][1]: 4,
          jogos[0][0]: 1}