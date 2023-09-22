def pontos_por_time(lista):
    patida1 = lista[0]
    partida2= lista[1]
    dici= {partida1[0]:0, partida2[0]:0}
          
    if partida1[2][0] > partida1[2][1]:
       dici[partida1[0]] += 3
    if partida1[2][0] == partida[2][1]:
       dici[partida1[0]] += 1
       dici[partida1[1]] +=1
    if partida1[2][0] < partida1[2][1]:
       dici[partida1[1]] +=3
    if partida2[2][0] > partida2[2][1]:
       dici[partida1[1]]+=3
    if partida2[2][0] ==partida2[2][1]:
       dici[partida1[1]]+=1
       dici[partida1[0]]+=1
    else:
       dici[partida1[0] +=3
            return dici