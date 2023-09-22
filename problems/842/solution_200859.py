def pontos_por_time(lista1):
                   """([[time1,time2,[gol_time1_ida,gol_time2_ida]],[time2,time1[gol_time2,gol_time1]]]:"""
                   time1=lista1[0][0]
                   time2=lista1[0][1]
                   gol_time1_ida=lista1[0][2][0]
                   gol_time2_ida=lista1[0][2][1]
                   gol_time2_volta=lista1[1][2][0]
                   gol_time1_volta=lista1[1][2][1]


                   if int(gol_time1_ida)>int(gol_time2_ida):
                       ponto1_ida=3
                   else:
                           ponto1_ida=0
                   if int(gol_time2_ida)>int(gol_time1_ida):
                       ponto2_ida=3
                   else:
                           ponto2_ida=0
                   if int(gol_time1_ida)==int(gol_time2_ida):
                       ponto_empate_ida=1
                   else:
                           ponto_empate_ida=0
                   if int(gol_time1_volta)>int(gol_time2_volta):
                       ponto1_volta=3
                   else:
                           ponto1_volta=0
                   if int(gol_time2_volta)>int(gol_time1_volta):
                       ponto2_volta=3
                   else:
                           ponto2_volta=0
                   if int(gol_time1_volta)==int(gol_time2_volta):
                       ponto_empate_volta=1
                   else:
                           ponto_empate_volta=0

                   pontos1=int(ponto1_ida) + int(ponto_empate_ida) + int(ponto1_volta) + int(ponto_empate_volta)
                   pontos2=int(ponto2_ida) + int(ponto_empate_ida) + int(ponto2_volta) + int(ponto_empate_volta)

                   return str({lista1[0][0]:int(pontos1),lista1[0][1]:int(pontos2)})