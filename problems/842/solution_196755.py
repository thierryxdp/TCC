def pontos_por_time(ls):
  # jogos
  j0 = ls[0]
  j1 = ls[1]
  # nomes
  t0_nome = j0[0]
  t1_nome = j0[1]
  d = {t0_nome: 0, t1_nome: 0} # meu retorno, a contabilidade dos pontos
  # considera o jogo de ida
  t0_pt, t1_pt = pontos(j0[2]) # [1, 0]
  # contabiliza
  d = contabiliza(d,  (t0_nome, t0_pt), (t1_nome, t1_pt) )
  # considera o jogo de volta
  t1_pt, t0_pt = pontos(j1[2])
  # contabiliza
  d = contabiliza(d, (t0_nome, t0_pt), (t1_nome, t1_pt) )
  return d

def contabiliza(d_ent, tup0, tup1):
  d = dict.copy(d_ent)
  nome0, pt0 = tup0
  nome1, pt1 = tup1
  d[nome0] += pt0
  d[nome1] += pt1
  return d

def pontos(gols):
  # init os pontos
  t0_pt = 0
  t1_pt = 0
  # faz o calculo
  t0_gols = gols[0]
  t1_gols = gols[1]
  if t0_gols > t1_gols:
    t0_pt += 3
  elif t1_gols > t0_gols:
    t1_pt += 3
  else:
    t0_pt += 1
    t1_pt += 1
  return (t0_pt, t1_pt)

#Start your python function here