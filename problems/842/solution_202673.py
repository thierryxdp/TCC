def pontos_por_time(lista):

  """
  Primeiro eu declarei duas variáiveis que representam o número de pontos de cada time e atráves de um sistema de if/elif/else foram acrescentando valores a essas variáveis de acordo com o resultado dos jogos de ida e de volta

  Depois disso eu criei um dicionário com o nome do time passado e o ponto dele e pro fim esse dicionário foi retornado
  """

  pontos_do_time_1 = 0
  pontos_do_time_2 = 0

  if lista[0][2][0] > lista[0][2][1]:

    pontos_do_time_1 = pontos_do_time_1 + 3

  elif lista[0][2][0] < lista[0][2][1]:

    pontos_do_time_2 = pontos_do_time_2 + 3

  else:

    pontos_do_time_1 = pontos_do_time_1 + 1
    pontos_do_time_2 = pontos_do_time_2 + 1

  if lista[1][2][0] > lista[1][2][1]:

    pontos_do_time_1 = pontos_do_time_1 + 3

  elif lista[1][2][0] < lista[1][2][1]:

    pontos_do_time_2 = pontos_do_time_2 + 3

  else:

    pontos_do_time_1 = pontos_do_time_1 + 1
    pontos_do_time_2 = pontos_do_time_2 + 1
    

  mapeamento_da_rodada = {lista[0][0]:pontos_do_time_1,lista[0][1]:pontos_do_time_2}

  return mapeamento_da_rodada