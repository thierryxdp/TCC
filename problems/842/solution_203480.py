def pontos_por_time(lista):
    x=str(time1)
    y=str(time2)
    pontos1=[a,b]
    pontos2=[c,d]
    jogo_ida=[time1,time2,pontos1]
    jogo_volta=[time2,time1,pontos2]
    lista=[jogo_ida,jogo_volta]
    if a>b or a<b:
         a*3 or b*3
    else:
          a*1 and b*1
    if c>d or a<d:
         c*3 or d*3
    else:
          c*1 and d*1
    total_pontos1=a+d
    total_pontos2=c+a
   return {time1[0]:total_pontos1,time2[1]:total_pontos2}