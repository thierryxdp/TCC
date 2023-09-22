def melhor_volta(matriz):
  x = -1
  tempos = []
  for i in matriz:
    x += 1
    tempos.append(min(i))
  return min(tempos)