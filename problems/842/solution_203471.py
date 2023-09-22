def pontos_por_time(lista):
    """Função que numero total de pontos de cada time dados
as informações do jogo da ida e jogo da volta; list -> dict"""
    time1=lista[0][0]
    cormengo_volta=lista[1][1]
    time2=lista[0][1]
    fla_volta=[1][0]
    gols_t1=lista[0][2][0]
    gols_t1f=lista[1][2][1]
    gols_t2=lista[0][2][1]
    gols_t2f=lista[1][2][0]
    pontos_t1=0
    pontos_t2=0
    vitoria=3
    empate=1
    if gols_t1>gols_t2:
        pontos_t1+=vitoria
    if gols_t1f>gols_t2f:
        pontos_t1+=vitoria
    if gols_t2>gols_t1:
        pontos_t2+=vitoria
    if gols_t2f>gols_t1f:
        pontos_t2+=vitoria
    if gols_t1==gols_t2:
        pontos_t1+=empate
        pontos_t2+=empate

    
    return {time1:pontos_t1,time2:pontos_t2}