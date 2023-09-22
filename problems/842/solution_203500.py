#Start your python function heredef pontos_por_time(lista):
    '''Essa função, dado uma lista de dois elementos, sendo esses elementos também uma lista,
    contendo o nome de dois times e seus respectivos número de gols cada, retorna um dicionário mapeando
    o time e seu respectivo número de pontos na fase, list->dict'''
    time1=str(lista[0][0])
    time2=str(lista[1][0])
    a=lista[0][2][0]
    b=lista[0][2][1]
    c=lista[1][2][0]
    d=lista[1][2][1]
    pontos1=[a,b]
    pontos2=[c,d]
    jogo_ida=[time1,time2,pontos1]
    jogo_volta=[time2,time1,pontos2]
    lista=[jogo_ida,jogo_volta]
    if a>b or a<b:
       pontos1[0],3 or b,3
    else:
         a,1 and b,1
    if c>d or c<d:
       c,3 or d,3
    else:
        c,1 and d,1
    total_pontos1=a+d
    total_pontos2=c+b
    return {time1:total_pontos1,time2:total_pontos2}