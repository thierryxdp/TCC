def pontos_por_time(Lista):
    """Recebe uma lista com dois elementos, sendo cada elemento uma lista,
     A lista contem, respectivamente, o nome do time da casa, de fora e os gols da partida.
     list->dict"""
    Jogodeida=Lista[0]
    Jogodevolta=Lista[1]
    time1=Jogo_ida[0]
    time2=Jogo_ida[1]
    gida=Jogodeida[2]
    gvolta=Jogodevolta[2]
    a1=gida[0]
    a2=gida[1]
    b2=gvolta[0]
    b1=gvolta[1]
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