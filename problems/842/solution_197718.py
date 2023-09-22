def pontos_por_time(l1,l2):
    'dados duas listas que fornecem informações sobre dois jogos de futebol, retorne o total de pontos que cada time fez na fase. lista,lista->dicio'
    v1=int()
    v2=int()
    e=int()
    time1=l1[0]
    time2=l1[1]
    
    if l1[2][0]>l1[2][1]:
        v1=3
    if l1[2][0]<l1[2][1]:
        v2=3
    if l1[2][0]==l1[2][1]:
        e=1
    if l2[2][0]>l2[2][1]:
        v1=3
    if l2[2][0]<l2[2][1]:
        v2=3
    if l2[2][0]==l2[2][1]:
        e=1
    return {time1:v1+e,time2:v2+e}