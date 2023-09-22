def pontos_por_time(jogo1,jogo2):
   if jogo1[2][0] > jogo1[2][1] and jogo2[2][0] > jogo2[2][1]:
     return [jogo1[0], 3, jogo2[0], 3]
   if jogo1[2][0] < jogo1[2][1] and jogo2[2][0] < jogo2[2][1]:
     return [jogo1[0], 3, jogo2[0], 3] 
   if jogo1[2][0] > jogo1[2][1] and jogo2[2][0] < jogo2[2][1]:
     return [jogo1[0], 6, jogo2[0], 0] 
   if jogo1[2][0] < jogo1[2][1] and jogo2[2][0] > jogo2[2][1]:
     return [jogo1[0], 0, jogo2[0], 6]
   if jogo1[2][0] > jogo1[2][1] and jogo2[2][0] == jogo2[2][1]:
     return [jogo1[0], 4, jogo2[0], 1]
   if jogo1[2][0] < jogo1[2][1] and jogo2[2][0] == jogo2[2][1]:
     return [jogo1[0], 1, jogo2[0], 4]
   if jogo1[2][0] == jogo1[2][1] and jogo2[2][0] == jogo2[2][1]:
     return [jogo1[0], 1, jogo2[0], 1]
   if jogo1[2][0] == jogo1[2][1] and jogo2[2][0] > jogo2[2][1]:
     return [jogo1[0], 1, jogo2[0], 4]
   else:
     return [jogo1[0], 4, jogo2[0], 1]