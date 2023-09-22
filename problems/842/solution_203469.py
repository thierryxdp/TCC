def pontos_por_time(lista):
    """Função que numero total de pontos de cada time dados
as informações do jogo da ida e jogo da volta; list -> dict"""
    jogo_ida=lista[0]
    jogo_volta=lista[1]
    time1=lista[0][0]
    cormengo_volta=lista[1][1]
    time2=lista[0][1]
    fla_volta=[1][0]
    gols_ci=lista[0][2][0]
    gols_cv=lista[1][2][1]
    gols_fi=lista[0][2][1]
    gols_fv=lista[1][2][0]
    pontos_c=0
    pontos_f=0
    vitoria=3
    empate=1
    if gols_ci>gols_fi:
        pontos_c+=vitoria
    if gols_cv>gols_fv:
        pontos_c+=vitoria
    if gols_fi>gols_ci:
        pontos_f+=vitoria
    if gols_fv>gols_ci:
        pontos_f+=vitoria
    if gols_ci==gols_fi:
        pontos_c+=empate
        pontos_f+=empate
    
    return {time1:pontos_c,time2:pontos_f}