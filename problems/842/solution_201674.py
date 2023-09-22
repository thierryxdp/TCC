def pontos_por_time(jogo1,jogo2):
    '''Após receber duas listas referentes a dois jogos, contendo cada uma os nomes dos dois times competidores
    e  uma lista com as pontuações de ambos em ordem, retorna um dicionário cujas chaves são os nomes de cada time e
    seus valores referentes são as pontuações totais deles ao fim dos dois jogos;
    entrada: lista, lista;
    saída: dicionário;
    '''
    pontuacao1 = [0]
    pontuacao2 = [0]
    if (jogo1[2][0]>jogo1[2][1]):
      pontuacao1 = [pontuacao1[0]+3]
    elif (jogo1[2][1]>jogo1[2][0]):
      pontuacao2 = [pontuacao2[0]+3]
    elif (jogo1[2][0]==jogo1[2][1]):
      pontuacao1 = [pontuacao1[0]+1]
      pontuacao2 = [pontuacao2[0]+1]
    if (jogo2[2][0]>jogo2[2][1]):
      pontuacao1 = [pontuacao1[0]+3]
    elif (jogo2[2][1]>jogo2[2][0]):
      pontuacao2 = [pontuacao2[0]+3]
    elif (jogo2[2][0]==jogo2[2][1]):
      pontuacao1 = [pontuacao1[0]+1]
      pontuacao2 = [pontuacao2[0]+1]
    placar ={jogo1[0]:str(pontuacao1),jogo1[1]:str(pontuacao2)}
    return placar