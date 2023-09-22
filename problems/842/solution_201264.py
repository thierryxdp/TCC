def pontos_por_time(fase):
    """Dados dois jogos entre dois times e os placares desses, retorna qual time tem mais pontos na fase"""
    nome_time1=fase[0][0]
    nome_time2=fase[0][1]
    placar_ida=fase[0][2]
    placar_volta=fase[1][2]
    pontos_time1=[]
    pontos_time2=[]
    if placar_ida[0]>placar_ida[1]:
        pontos_time1=[3]
    if placar_volta[1]>placar_volta[0]
        pontos_time1+=3
    if placar_ida[0]=placar_ida[1]:
        pontos_time1+=1
    if placar_volta[1]=placar_volta[0]:
        pontos_time1+=1
    if placar_ida[1]>placar_ida[0]:
        pontos_time2+=3
    if placar_volta[0]>placar_volta[1]:
        pontos_time2+=3
    if placar_ida[0]=placar_ida[1]:
        pontos_time2+=1
    if placar_volta[1]=placar_volta[0]:
        pontos_time2+=1
    return {nome_time1:pontos_time1,nome_time2:pontos_time2}