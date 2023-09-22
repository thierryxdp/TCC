def pontos_por_time(lista):
    '''Essa função, dado uma lista de dois elementos, sendo esses elementos também uma lista,
    contendo o nome de dois times e seus respectivos número de gols cada, retorna um dicionário mapeando
    o time e seu respectivo número de pontos na fase, list->dict'''
    time1=str(lista[0][0])
    time2=str(lista[1][0])
    a=(lista[0][2][0])
    b=(lista[0][2][1])
    c=(lista[1][2][0])
    d=(lista[1][2][1])
    pontos1=[a,b]
    pontos2=[c,d]
    placar1=0
    placar2=0
    if a>b:
       a=placar1+3
       b=placar2+b
    elif a<b:
         b=placar2+3
         a=placar1+a
    else:
        a=placar1+1
        b=placar2+1
    if c>d:
       c=placar1+3
       d=placar2+d
    elif c<d:
         d=placar2+3
         c=placar1+c
    else:
        c=placar1+1
        d=placar2+1
    total_pontos1=a+d
    total_pontos2=c+b
    return {time1:total_pontos1,time2:total_pontos2}