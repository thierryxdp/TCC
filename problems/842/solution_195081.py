def pontos_por_time(Lista):
    '''list->dict'''
    L1=Lista[0]
    L2=Lista[1]
    time1=L1[0]
    time2=L1[1]
    pida=L1[2]
    pvolta=L2[2]
    x1=pida[0]
    x2=pida[1]
    y2=pvolta[0]
    y1=pvolta[1]
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