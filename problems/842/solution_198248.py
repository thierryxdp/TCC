def pontos_por_time(lista):
    jogo1 = lista.pop(0)
    pjogo2 = lista[:1]
    jogo2 = pjogo2.pop(0)
    time1 = str(jogo1[0])
    time2 = str(jogo1[1])
    resultado1 = jogo1.pop(2)
    resultado2 = jogo2.pop(2)
    total_de_pontos_Mengo_Roda1 = []
    if resultado1[0] > resultado1[1]:
        x = 3
    elif resultado1[0] == resultado1[1]:
        x = 1
    else:
        x = 0
    total_de_pontos_Mengo_Roda1 = int(x)

    total_de_pontos_Mengo_Roda2 = []
    if resultado2[0] < resultado2[1]:
        y = 3
    elif resultado2[0] == resultado2[1]:
        y = 1
    else:
        y = 0
    total_de_pontos_Mengo_Roda2 = int(y)

    total_de_pontos_Mengo_Roda = total_de_pontos_Mengo_Roda1 + total_de_pontos_Mengo_Roda2
    
    total_de_pontos_Corin_Roda1 = []
    if resultado1[0] < resultado1[1]:
        total_de_pontos_Corin_Roda1 = 3
    elif resultado1[0] == resultado1[1]:
        total_de_pontos_Corin_Roda1 = 1
    else:
        total_de_pontos_Corin_Roda1 = 0

    total_de_pontos_Corin_Roda2 = []
    if resultado2[0] > resultado2[1]:
        total_de_pontos_Corin_Roda2 = 3
    elif resultado2[0] == resultado2[1]:
        total_de_pontos_Corin_Roda2 = 1
    else:
        total_de_pontos_Corin_Roda2 = 0

    total_de_pontos_Corin_Roda = total_de_pontos_Corin_Roda1 + total_de_pontos_Corin_Roda2

    timet1 = []
    if str(time2) in ['Paulo da Gama']:
        timet1 = time1
    elif str(time1) in ['Paulo da Gama','Flumipaulo','Botagama','Santasco','Fluminantos','Vasínthians']:
       timet1 = time2
    else:
        timet1 = time1

    timet2 = []
    if str(time2) in ['Paulo da Gama']:
        timet2 = time2
    elif str(time1) in ['Paulo da Gama','Flumipaulo','Botagama','Santasco','Fluminantos','Vasínthians']:
        timet2 = time1
    else:
        timet2 = time2 
    total1 = []
    if str(time2) in ['Paulo da Gama']:
        total1 = total_de_pontos_Mengo_Roda
    elif str(time1) in ['Paulo da Gama','Flumipaulo','Botagama','Santasco','Fluminantos','Vasínthians']:
       total1 = total_de_pontos_Corin_Roda
    else:
       total1 = total_de_pontos_Mengo_Roda 
    total2 = []
    if str(time2) in ['Paulo da Gama']:
        total2 = total_de_pontos_Corin_Roda
    elif str(time2) in ['Fluminantos','Santense','Cornense','Fluminantos','Botameiras','Santeiras']:
       total2 = total_de_pontos_Mengo_Roda
    else:
       total2 = total_de_pontos_Corin_Roda 
    tabela = {
        str(timet1) : total1,
        str(timet2) : total2
        }
    return tabela