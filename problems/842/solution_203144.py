def pontos_por_time(lista):
  '''Função que recebe uma lista de 2 elementos (jogo ida e jogo de volta), onde cada elemento é também uma lista (contendo qtd. gols), 
  e retorna um dicionário cujos mapeamentos são os times e seus respectivos pontos totais.
  list -> list'''

  #Lista recebida pela função contém 2 elementos (listas com informações dos jogos)
  listaJ1 = lista[0]
  listaJ2 = lista[1]
  placar1 = listaJ1[2]
  placar2 = listaJ2[2]

  soma_pontos_C = 0
  soma_pontos_F = 0

  if len(lista) == 2:
    if listaJ1[0] == 'Cormengo' and listaJ1[1] == 'Flamínthians':
      if placar1[0] > placar1[1]:
        soma_pontos_C += 3
      elif placar1[0] < placar1[1]:
        soma_pontos_F += 3
      elif placar1[0] == placar1[1]:
        soma_pontos_C += 1
        soma_pontos_F += 1

    if listaJ2[0] == 'Flamínthians' and listaJ2[1] == 'Cormengo':
      if placar2[0] > placar2[1]:
        soma_pontos_F += 3
      elif placar2[0] < placar2[1]:
        soma_pontos_C += 3
      elif placar2[0] == placar2[1]:
        soma_pontos_F += 1
        soma_pontos_C += 1

  dicionario = {'Cormengo': soma_pontos_C, 'Flaminthians': soma_pontos_F}

  return dicionario