def pontos_por_time(Lista):
    """Recebe uma lista com dois elementos, sendo cada elemento uma lista,
    A lista contem, respectivamente, o nome do time da casa, de fora e os gols da partida.
    Retorna o numero de pontosna fase de cada time.
    list->dict"""
    
    Jogo_ida=Lista[0]
    Jogo_volta=Lista[1]
    n_time1=Jogo_ida[0]
    n_time2=Jogo_ida[1]
    gols_ida=Jogo_ida[2]
    gols_volta=Jogo_volta[2]
    if gols_ida[0]>gols_ida[1] and gols_volta[0]>gols_volta[1]:
        pont1=6
        pont2=0
    elif gols_ida[0]>gols_ida[1] and gols_volta[0]==gols_volta[1] or gols_ida[0]==gols_ida[1] and gols_volta[0]>gols_volta[1]:
        pont1=4
        pont2=1
    elif gols_ida[0]==gols_ida[1] and gols_volta[0]==gols_volta[1]:
        pont1=2
        pont2=2
    elif gols_ida[0]<gols_ida[1] and gols_volta[0]>gols_volta[1] or gols_ida[0]>gols_ida[1] and gols_volta[0]<gols_volta[1]:
        pont1=3
        pont2=3
    elif gols_ida[0]==gols_ida[1] and gols_volta[0]<gols_volta[1] or gols_ida[0]<gols_ida[1] and gols_volta[0]==gols_volta[1]:
        pont1=1
        pont2=4
    elif  gols_ida[0]<gols_ida[1] and gols_volta[0]<gols_volta[1]:
        pont1=0
        pont2=6
    return {n_time1:pont1,n_time2:pont2}