def pontos_por_time(ls):
  d = {}
  jogo1 = ls[0]
  jogo2 = ls[1]
  t1 = jogo1[0]
  t2 = jogo1[1]
  gols = jogo1[2]
  # análise do jogo 1
  t1_gols = gols[0]
  t2_gols = gols[1]
  if t1_gols == t2_gols:
    d[t1] = 1
    d[t2] = 1
  if t1_gols > t2_gols:
    d[t1] = 3
    d[t2] = 0
  if t1_gols < t2_gols:
    d[t1] = 0
    d[t2] = 3
  # análise do jogo 2
  gols = jogo2[2]
  t2_gols = gols[0]
  t1_gols = gols[1]
  if t1_gols == t2_gols:
    d[t1] = d[t1] + 1
    d[t2] = d[t2] + 1
  if t1_gols > t2_gols:
    d[t1] = d[t1] + 3
    d[t2] = d[t2] + 0
  if t1_gols < t2_gols:
    d[t1] = d[t1] + 0
    d[t2] = d[t2] + 3
  return d