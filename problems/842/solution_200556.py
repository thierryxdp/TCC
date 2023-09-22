def pontos_por_time(lista):
    '''Função que recebe uma lista de dois elementos,
    onde cada um desses elementos também são listas.
    Essa função retorna os pontos dos times.list->list'''
    time1=lista[0][0]
    time2=lista[0][1]
    pontostime1=0
    pontostime2=0
    golstime1vs1=lista[0][2][0]
    golstime2vs1=lista[0][2][1]
    golstime1vs2=lista[1][2][1]
    golstime2vs2=lista[1][2][0]
    if golstime1vs1>golstime2vs1:
        pontostime1=pontostime1+3
    if golstime1vs1<golstime2vs1:
        pontostime2+=3
    if golstime1vs1==golstime2vs1:
        pontostime1=1
        pontostime2=1
    if golstime1vs2>golstime2vs2:
        pontostime1=pontostime1+3
    if golstime1vs2<golstime2vs2:
        pontostime2+=3
    if golstime1vs2==golstime2vs2:
        pontostime1+=1
        pontostime2+=1
    return{time1:pontostime1,time2:pontostime2}