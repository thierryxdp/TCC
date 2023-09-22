def pontos_por_time(lista):
    '''funçao que recebe uma lista de dois elementos, onde cada elemento tambem é uma
lista, contendo asinformaçoes de numeros de gols em dois jogos de futebol entre dois times'''
    time1=lista[0][0]
    time2=lista[0][1]
    pomtost1=0
    pontost2=0
    golstime1p1=lista[0][2][0]
    golstime1p2=lista[1][2][1]
    golstime2p1=lista[0][2][1]
    golstimep22=lista[1][2][0]
    if golstime1p1>golstime2p1:
        pomtost1+=3
    if golstime2p1>golstime1p1:
        pomtost1+=3
    if golstime2p1==golstime1p1:
        pomtost1+=1
        pomtost1+=1
    if golstime1p2>golstime2p2:
        pomtost1+=3
    if golstime2p2>golstime1p2:
        pomtost1+=3
    if golstime2p2==golstime1p2:
        pomtost1+=1
        pomtost1+=1
    return{time1:pontost1,time2;pontost2}