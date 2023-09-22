def pontos_por_time(jogos):
    '''retorna um dicionario com o nome e os pontos de cada time dados os resultados de dois jogos entre eles'''
    gols_c_ida=jogos[0][2][0]
    gols_f_ida=jogos[0][2][1]
    
    gols_c_volta=jogos[1][2][0]
    gols_f_volta=jogos[1][2][1]

    
    if gols_c_ida > gols_f_ida:
      if gols_c_volta < gols_f_volta:
        return {jogos[0][0]:6, jogos[0][1]:0}
      elif gols_c_volta > gols_f_volta:
        return {jogos[0][0]:3, jogos[0][1]:3}
      else:
        return {jogos[0][0]:4, jogos[0][1]:1}
    elif gols_c_ida < gols_f_ida:
      if gols_c_volta < gols_f_volta:
        return {jogos[0][0]:3, jogos[0][1]:3}
      elif gols_c_volta > gols_f_volta:
        return {jogos[0][0]:0, jogos[0][1]:6}
      else:
        return {jogos[0][0]:1, jogos[0][1]:4}
    else:
      if gols_c_volta < gols_f_volta:
        return {jogos[0][0]:4, jogos[0][1]:1}
      elif gols_c_volta > gols_f_volta:
        return {jogos[0][0]:1, jogos[0][1]:4}
      else:
        return {jogos[0][0]:2, jogos[0][1]:2}