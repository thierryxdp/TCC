#Start your python function here
def pontos_por_time(lista=[(time,gols),(time,gols)]):
  time={lista[0][0]:0,lista[0][1]:0}
  gols0=lista[0][2]

  if gols0[0]>gols0[1]:
   time[lista[0][1]]+=3
  if gols0[1]>gols0[0]:
   time[lista[0][0]]+=3
  if gols0[1]== gols0[1]:
   time[lista[0][0]]+=1
   time[lista[0][1]]+=1

   gols1=lista[1][2]
  if gols1[0]>gols1[1]:
   time[lista[0][1]]+=3
  if gols1[1]>gols1[0]:
   time[lista[0][0]]+=3
  if gols1[1]== gols1[1]:
   time[lista[0][0]]+=1
   time[lista[0][1]]+=1
                    
   return lista