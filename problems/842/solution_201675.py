def pontos_por_time(jogos):
    '''Após receber duas listas referentes a dois jogos, contendo cada uma os nomes dos dois times competidores
    e  uma lista com as pontuações de ambos em ordem, retorna um dicionário cujas chaves são os nomes de cada time e
    seus valores referentes são as pontuações totais deles ao fim dos dois jogos;
    entrada: lista, lista;
    saída: dicionário;
    '''
    pontuacao1 = [0]
    pontuacao2 = [0]
    if (jogos[0][2][0]>jogos[0][2][1]):
      pontuacao1 = [pontuacao1[0]+3]
    elif (jogos[0][2][1]>jogos[0][2][0]):
      pontuacao2 = [pontuacao2[0]+3]
    elif (jogos[0][2][0]==jogos[0][2][1]):
      pontuacao1 = [pontuacao1[0]+1]
      pontuacao2 = [pontuacao2[0]+1]
    if (jogos[1][2][0]>jogos[1][2][1]):
      pontuacao1 = [pontuacao1[0]+3]
    elif (jogos[1][2][1]>jogos[1][2][0]):
      pontuacao2 = [pontuacao2[0]+3]
    elif (jogos[1][2][0]==jogos[1][2][1]):
      pontuacao1 = [pontuacao1[0]+1]
      pontuacao2 = [pontuacao2[0]+1]
    placar ={jogos[0][0]:str(pontuacao1),jogos[0][1]:str(pontuacao2)}
    return placar