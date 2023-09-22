def pontos_por_time(Lista):
    """Recebe uma lista com dois elementos, sendo cada elemento uma lista,
     A lista contem, respectivamente, o nome do time da casa, de fora e os gols da partida.
     list->dict"""
    Jogodeida=Lista[0]
    Jogodevolta=Lista[1]
    n_time1=Jogodeida[0]
    n_time2=Jogodeida[1]
    jida=Jogodeida[2]
    jvolta=Jogodevolta[2]
    a1=jida[0]
    a2=jida[1]
    b2=jvolta[0]
    b1=jvolta[1]
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
        
    return {n_time1:pont1,n_time2:pont2}