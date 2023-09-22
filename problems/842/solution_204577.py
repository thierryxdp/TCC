def pontos_por_time(lista):
  """
  """
  pontosjogo1a = 0
    
  pontosjogo1b = 0

  if lista[0][2][0]>lista[0][2][1]:
    pontosjogo1a += 3
  elif lista[0][2][1]>lista[0][2][0]:
    pontosjogo1b += 3
  elif lista[0][2][0] == lista[0][2][1]:
    pontosjogo1a += 1
    pontosjogo1b += 1
  elif lista[1][2][0]>lista[1][2][1]:
    pontosjogo1b += 3
  elif lista[1][2][1]>lista[1][2][0]:
    pontosjogo1a += 3
  elif lista[1][2][0] == lista[1][2][1]:
    pontosjogo1a += 1
    pontosjogo1b += 1
  return {lista[0][0]: pontosjogo1a, lista[0][1]: pontosjogo1b}