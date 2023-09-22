def pontos_por_time(Lista):
    Jogo_ida=Lista[0]
    Jogo_volta=Lista[1]
    n_time1=Jogo_ida[0]
    n_time2=Jogo_ida[1]
    gida=Jogo_ida[2]
    gvolta=Jogo_volta[2]
    1a=gida[0]
    2a=gida[1]
    1b=gvolta[0]
    2b=gvolta[1]
    if 1a>2a and 1b>2b:
        pont1=6
        pont2=0
    elif 1a>2a and 1b==2b or 1a==2a and 1b>2b:
        pont1=4
        pont2=1
    elif 1a==2a and 1b==2b:
        pont1=2
        pont2=2
    elif 1a<2a and 1b>2b or 1a>2a and 1b<2b:
        pont1=3
        pont2=3
    elif 1a==2a and 1b<2b or 1a<2a and 1b==2b:
        pont1=1
        pont2=4
    else:
        pont1=0
        pont2=6
        
    return {n_time1:pont1,n_time2:pont2}