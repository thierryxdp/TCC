def pontos_por_time(fase):
  #dividindo a lista pra facilitar a manipulação
  ida = fase[0]
  volta = fase[1]

  #declarando as variaveis necessarias
  gols_cormengo_ida = 0 
  gols_flaminthians_ida = 0
  gols_cormengo_volta = 0 
  gols_flaminthians_volta = 0
  pontos_cormengo = 0
  pontos_flaminthians = 0
  empate = 1
  vitoria = 3

  
  #somando os gols da ida
  if (ida[0]) == 'Cormengo':
      gols_cormengo_ida += int(ida[2][0])
      gols_flaminthians_ida += int(ida[2][1])
  else:
      gols_flaminthians_ida += int(ida[2][0])
      gols_cormengo_ida += int(ida[2][1])

  #verificando o resultado e a pontuacao da ida
  if (gols_cormengo_ida > gols_flaminthians_ida):
      pontos_cormengo += vitoria
  elif (gols_flaminthians_ida > gols_cormengo_ida):
      pontos_flaminthians += vitoria
  else:
      pontos_flaminthians += empate
      pontos_cormengo += empate

  #somando os gols da volta
  if(volta[0]) == 'Cormengo':
      gols_cormengo_volta += int(volta[2][0])
      gols_flaminthians_volta += int(volta[2][1])
  else:
      gols_flaminthians_volta += int(volta[2][0])
      gols_cormengo_volta += int(volta[2][1])

  #verificando o resultado e a pontuacao da volta
  if (gols_cormengo_volta > gols_flaminthians_volta):
      pontos_cormengo += vitoria
  elif (gols_flaminthians_volta > gols_cormengo_volta):
      pontos_flaminthians += vitoria
  else:
      pontos_flaminthians += empate
      pontos_cormengo += empate

  #criando o dicionario
  dic = {"Cormengo": pontos_cormengo, "Flamínthians": pontos_flaminthians}

  print(dic)
  return dic
  
pontos_por_time([['Cormengo', 'Flamínthians', [1,0]], ['Flamínthians', 'Cormengo', [2,2]]])