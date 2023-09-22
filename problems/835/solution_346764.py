def melhor_volta(corrida):
   '''Retorna uma tupla com a melhor volta
       da prova, quanto tempo teve e em que
       volta; matriz de 6x10->tuple'''
   melhorVolta=corrida[0][0]
   i=0
   for desempenho in corrida:
      tempo=min(desempenho)
      if tempo<melhorVolta:
         corredor=i+1
         volta=list.index(desempenho,tempo)+1
      i+=1   
   return corredor, tempo, volta