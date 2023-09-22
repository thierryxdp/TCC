def pontos_por_time(l):
    'dado uma lista contendo dois elementos do tipo lista que fornecem informações sobre dois jogos de futebol, retorne um dicionario com o total de pontos que cada time fez na fase. lista->dicio'
    v1=int()
    v2=int()
    e=int()
    time1=l[0][0]
    time2=l[0][1]
    
    if l[0][2][0]>l[0][2][1]:
        v1=3
    if l[0][2][0]<l[0][2][1]:
        v2=3
    if l[0][2][0]==l[0][2][1]:
        e=1
    if l[1][2][0]>l[1][2][1]:
        v1=3
    if l[1][2][0]<l[1][2][1]:
        v2=3
    if l[1][2][0]==l[1][2][1]:
        e=1
    return {time1:v1+e,time2:v2+e}