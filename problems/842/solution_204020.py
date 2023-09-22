def pontos_por_time(lista):
    '''retorna um dicionario com o mapeamento <nome do time> -> <numero total de pontos fase>'''
    gol_ida1=lista[0][2][0]
    gol_ida2=lidta[0][1][1]
    gol_volta2=lista[1][2][0]
    gol_volta1=lista[1][2][1]
    
    if gol_ida1>gol_ida2:
        pontos_ida1=3
        pontos_ida2=0
    elif gol_ida1==gol_ida2:
            pontos_ida1=1
            pontos_ida2=1
    else:
        pontos_ida1=0