def pontos_por_time(lista1, lista2):
	'''list,list->dict'''
    partida_ida= lista1
    partida_volta= lista2
    partidas= {partida_ida[0]:0,partida_ida[1]:0}

    if partida_ida[0]>partida_ida[1]:
        partidas[partida_ida[0]]=partidas[partida_ida[0]] +3
    if partida_ida[0]<partida_ida[1]:
        partidas[partida_ida[1]]=partidas[partida_ida[1]] +3
    if partida_ida[0]==partida_ida[1]:
        partidas[partida_ida[0] +1 and partidas[partida_ida[1] +1
return partidas