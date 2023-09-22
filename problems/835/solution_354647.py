def melhor_volta(matriz):
  x = -1
  volta = 0
  tempos = []
  idx_ganhador = []
  for i in matriz:
    x += 1
    tempos.append(min(i))
    idx_ganhador.append(matriz[x].index(min(i)))
  return (tempos.index(min(tempos))+1,min(tempos),idx_ganhador[tempos.index(min(tempos))]+1)