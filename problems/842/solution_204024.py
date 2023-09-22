def pontos_por_time (lista):
    nome_time1=lista[0][0]
    nome_time2=lista[0][1]
    gol_ida1=lista[0][2][0]
    gol_ida2=lista[0][2][1]
    gol_volta1=lista[1][2][1]
    gol_volta2=lista[1][2][0]
    if gol_ida1>gol_ida2:
        pontos_ida1=3
        pontos_ida2=0
	elif gol_ida1<gol_ida2:
        pontos_ida1=0
        pontos_ida2=3
    else:
        pontos_ida1=1
        pontos_ida2=1
    if gol_volta1>gol_volta2:
        pontos_volta1=3
        pontos_volta2=0
	elif gol_volta1<gol_volta2:
        pontos_volta1=0
        pontos_volta2=3
    else:
        pontos_volta1=1
        pontos_volta2=1
    pontos_total1=pontos_ida1+pontos_volta1
    pontos_total2=pontos_ida2+pontos_volta2  
    return {nome_time1:pontos_total1,nome_time2:pontos_total2}