def pontos(campeonato):
  '''Função que receba uma lista de dois elementos, onde cada um desses elementos é também uma lista. A lista completa tem informações do número de gols em dois jogos de futebol entre dois times, cada lista vem o nome dos dois times e o placar nessa ordem, e retorna o nome do time e a soma do pontos
   lista,lista -> dicionario'''
  jogo_ida = campeonato[0] 
  jogo_volta=campeonato[1]
  
  mandante = jogo_ida[0]
  visitante = jogo_ida[1]
  
  placar_ida = jogo_ida[2]

  
  gols_mandante = placar_ida[0]
  gols_visitante = placar_ida[1]
  placar_volta = jogo_volta[2]
  gols_visitante = placar_volta[0]
  gols_mandante = placar_volta[1]
  
  pontos_mandante = 0
  pontos_visitante = 0
  
  if placar_ida[0]>placar_ida[1]:
    pontos_mandante += 3
  
  if placar_ida[0]<placar_ida[1]:
    pontos_visitante += 3
  
  if placar_ida[0]==placar_ida[1]:
     pontos_mandante += 1
     pontos_visitante += 1
  
  if placar_volta[0]>placar_volta[1]:
   pontos_visitante +=3

  if placar_volta[0] < placar_volta[1]:
    pontos_mandante += 3
  
  if placar_volta[0] == placar_volta[1]:
    pontos_mandante += 1
    pontos_visitante += 1

  return{jogo_ida[0]: pontos_mandante , jogo_ida[1]: pontos_visitante}