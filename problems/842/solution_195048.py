def pontos_por_time(Lista):
    '''recebe como entrada uma lista,onde cada elemento dessa lista é tambem uma lista contendo:nome do time1,time dois e uma
    lista com placar do jogo de ida, e uma segunda lista com os nomes do time1,time2, e o placar do jogo de volta.A funcão
    retorna um dicionario com o total de pontos e os nomes do time'''
    L1=Lista[0]
    L2=Lista[1]
    time1=L1[0]
    time2=L1[1]
    pontosida=L1[2]
    pontosvolta=L2[2]
    x1=pontosida[0]
    x2=pontosida[1]
    y1=pontosvolta[0]
    y2=pontosvolta[1]
    if x1>x2 and y1>y2:
        pont1=6
        pont2=0
    elif x1>x2 and y1==y2 or x1==x2 and y1>y2:
        pont1=4
        pont2=1
    elif x1==x2 and y1==y2:
        pont1=2
        pont2=2
    elif x1<x2 and y1>y2 or x1>x2 and y1<y2:
        pont1=3
        pont2=3
    elif x1==x2 and y1<y2 or x1<x2 and y1==y2:
        pont1=1
        pont2=4
    else:
        pont1=0
        pont2=6
        
    return {time1:pont1,time2:pont2}