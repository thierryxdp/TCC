def pontos_por_time(lista):
    '''Retorna um dicionário de mapeamentos: <nome do time> -> <número
    total de pontos na fase>, a partir de uma lista=[['time1', 'time2',
    resultado], ['time2', 'time1', resultado2]];
    list[list[str,str,list[int,int],list[str,str,list[int,int]] -> 
    dict{str, int}'''
    nome1 = lista[0][0]
    if lista[0][2][0]<lista[0][2][1]:
        pontos1=0
    elif lista[0][2][0]==lista[0][2][1]:
        pontos1=1
    else:
        pontos1=3
    if lista[1][2][0]>lista[1][2][1]:
        pontos1=pontos1+0
    elif lista[1][2][0]==lista[1][2][1]:
        pontos1=pontos1+1
    else:
        pontos1=pontos1+3
    nome2 = lista[1][0]
    if lista[0][2][0]>lista[0][2][1]:
        pontos2=0
    elif lista[0][2][0]==lista[0][2][1]:
        pontos2=1
    else:
        pontos2=3
    if lista[1][2][0]<lista[1][2][1]:
        pontos2=pontos2+0
    elif lista[1][2][0]==lista[1][2][1]:
        pontos2=pontos2+1
    else:
        pontos2=pontos2+3
    return {nome1:pontos1,nome2:pontos2}