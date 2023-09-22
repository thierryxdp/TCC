def pontos_por_time(lista):
    Jogodeida=lista[0]
    Jogodevolta=lista[1]
    time1=Jogodeida[0]
    time2=Jogodeida[1]
    y=Jogodeida[2]
    x=Jogodevolta[2]
    a1=y[0]
    a2=y[1]
    b2=x[0]
    b1=x[1]
    if a1>a2 and b1>b2:
        pont1=6
        pont2=0
    elif a1>a2 and b1==b2 or a1==a2 and b1>b2:
        pont1=4
        pont2=1
    elif a1==a2 and b1==b2:
        pont1=2
        pont2=2
    elif a1<a2 and b1>b2 or a1>a2 and b1<b2:
        pont1=3
        pont2=3
    elif a1==a2 and b1<b2 or a1<a2 and b1==b2:
        pont1=1
        pont2=4
    else:
        pont1=0
        pont2=6
        
    return {time1:pont1,time2:pont2}