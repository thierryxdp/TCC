def pontos_por_time(lista):
  pontuacaotime1 = 0
  pontuacaotime2 = 0
  dicionario = {}
  if lista[0][2][0] > lista[0][2][1]:
    pontuacaotime1 = pontuacaotime1 +3 
  if lista[0][2][0] < lista[0][2][1]:
    pontuacaotime2 = pontuacaotime2 +3
  if lista[0][2][0] == lista[0][2][1]:
    pontuacaotime2 = pontuacaotime2 +1
    pontuacaotime1 = pontuacaotime1 +1
  if lista[1][2][1] > lista[1][2][0]:
    pontuacaotime1 = pontuacaotime1 +3 
  if lista[1][2][1] < lista[1][2][0]:
    pontuacaotime2 = pontuacaotime2 +3
  if lista[1][2][1] == lista[1][2][0]:
    pontuacaotime2 = pontuacaotime2 +1
    pontuacaotime1 = pontuacaotime1 +1
  dicionario[lista[0][0]] = pontuacaotime1
  dicionario[lista[0][1]] = pontuacaotime2
  return dicionario